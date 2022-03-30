import json
import logging
import datetime
from consts.platform import PLATFORM_NAME, PLATFORM_VERSION
from library.host import HostIp

class JSONFormatter(logging.Formatter):
    host_name, host_ip = HostIp.get_host_ip()
    # REMOVE_ATTR = ["filename", "module", "exc_text", "stack_info", "created", "msecs", "relativeCreated", "exc_info", "msg"]
    REMOVE_ATTR = []

    def format(self, record):
        extra = self.build_record(record)
        self.set_format_time(extra)
        self.set_host_ip(extra)
        self.set_platform_info(extra)
        extra['message'] = record.msg
        if record.exc_info:
            extra['exc_info'] = self.formatException(record.exc_info)
        if self._fmt == 'pretty':
            return json.dumps(extra, indent=1, ensure_ascii=False)
        else:
            return json.dumps(extra, ensure_ascii=False)

    @classmethod
    def build_record(cls, record):
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in cls.REMOVE_ATTR
        }

    @classmethod
    def set_format_time(cls, extra):
        now = datetime.datetime.utcnow()
        format_time = now.strftime("%Y-%m-%dT%H:%M:%S" + ".%03d" % (now.microsecond / 1000) + "Z")
        extra['@timestamp'] = format_time
        return format_time

    @classmethod
    def set_host_ip(cls, extra):
        extra['host_name'] = JSONFormatter.host_name
        extra['host_ip'] = JSONFormatter.host_ip
    
    @classmethod
    def set_platform_info(cls, extra):
        extra["platform_name"] = PLATFORM_NAME
        extra["platform_version"] = PLATFORM_VERSION
