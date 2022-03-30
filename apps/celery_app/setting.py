#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-03-29 20:30:41
# @Author  : Elijahxb (xbelijah@gmail.com)
# @Link    : www.junyipan.top:8090
# @Version : 1.0.0
# @Refer   : https://meiwencun.com/celery_pei_zhi_xuan_xiang_xiao_xie_488/
from kombu import Exchange, Queue

# 后端
broker_url = 'redis://127.0.0.1:6379/1'
result_backend = 'redis://127.0.0.1:6379/2'
broker_connection_retry=False
broker_pool_limit = 0
broker_heartbeat = 10
broker_connection_timeout = 30

# 结果处理
task_serializer = 'json'
result_serializer = 'json'
result_compression = "zlib"


# 超时配置
event_queue_expires = 60
result_expire = 60 * 10

# 默认路由
task_default_queue='default',
task_default_exchange='default',
result_exchange='default',

timezone = 'Asia/Shanghai'
enable_utc = False

# 限流
# task_annotations = {'*': {'rate_limit': '10/m'}}
task_annotations = {'apps.celery_app.processor.math.add': {'rate_limit': '10/m'}}
worker_prefetch_multiplier = 1

# 队列
task_queues = (
    Queue(name="math", exchange=Exchange(name="math", type="direct"), routing_key="math"),
    Queue(name="default", exchange=Exchange(name="default", type="direct"), routing_key="default")
)

# 路由
task_routes = {
    "default":{
      "queue": "default",
      "routing_key": "default"  
    },
    'apps.celery_app.processor.math.add': {
        'queue': 'math',
        'routing_key': 'math.add',
        'serializer': 'json',
    },
}