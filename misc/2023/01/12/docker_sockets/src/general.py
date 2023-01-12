from socket import *
import configparser
import os
import argparse

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
        self._server_host = CONFIG_GEN["server_host"]
        self._server_port = CONFIG_GEN.getint("server_port")

    def run(self):
        raise NotImplementedError


CONFIG_SVR = CONFIG["Server"]


class Server(Socketer):
    def __init__(self):
        super().__init__()
        self._server_socket.bind(("localhost", self._server_port))
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


CONFIG_CLI = CONFIG["Client"]


class Client(Socketer):
    def __init__(self):
        super().__init__()
        self._buf_size = CONFIG_CLI.getint("buf_size")

    def run(self):
        sock = self._server_socket
        sock.connect((self._server_host, self._server_port))
        sock.send(b"Hello!\n")
        data = sock.recv(1024)
        sock.close()
        print(repr(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--type",
        default="client",
    )
    args = parser.parse_args()
    app: Socketer | None = None
    if args.type == "client":
        app = Client()
    elif args.type == "server":
        app = Server()
    else:
        raise KeyError
    app.run()
