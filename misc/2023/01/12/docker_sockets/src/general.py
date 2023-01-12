from socket import *
import configparser
import os

CONFIG = configparser.ConfigParser()
CONFIG.read(os.environ.get("DS_INI", "config.ini"))

CONFIG_GEN = CONFIG["General"]


class Socketer:
    @staticmethod
    def _create_server_socket() -> socket:
        l3_protocol_str = CONFIG_GEN["L3_protocol"]
        l3_protocol = AddressFamily[l3_protocol_str]
        l4_protocol_str = CONFIG_GEN["L4_protocol"]
        l4_protocol = SocketKind[l4_protocol_str]
        sock = socket(l3_protocol, l4_protocol)
        return sock

    def __init__(self):
        self._server_socket = Socketer._create_server_socket()
        server_host = CONFIG_GEN["server_host"]
        server_port = CONFIG_GEN.getint("server_port")
        self._server_socket.bind((server_host, server_port))

    def run(self):
        raise NotImplementedError


CONFIG_SVR = CONFIG["Server"]


class Server(Socketer):
    def __init__(self):
        super().__init__()
        queue_size = CONFIG_SVR.getint("queue_size")
        self._server_socket.listen(queue_size)
        self._buf_size = CONFIG_SVR.getint("buf_size")

    def run(self):
        sock = self._server_socket
        while True:
            conn, addr = sock.accept()
            while True:
                data = conn.recv(self._buf_size)
                if not data:
                    break
                print(repr(data))
                conn.sendall(data)
            conn.close()
