import socket
class HostIp(object):
    @staticmethod
    def get_host_ip():
        hostname = socket.gethostname()
        return hostname, socket.gethostbyname(hostname)


if __name__ == "__main__":
    print(HostIp.get_host_ip())
