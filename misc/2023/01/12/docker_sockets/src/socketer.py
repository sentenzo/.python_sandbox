from socket import *
import configparser
import os

CONFIG = configparser.ConfigParser()
CONFIG.read(os.environ.get("DS_INI", "config.ini"))

CONFIG_GEN = CONFIG["General"]
CONFIG_SVR = CONFIG["Server"]
CONFIG_CLI = CONFIG["Client"]


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
        self._server_host = CONFIG_GEN["server_host"]
        self._server_port = CONFIG_GEN.getint("server_port")

    def run(self):
        raise NotImplementedError
