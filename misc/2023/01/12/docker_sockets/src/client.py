from time import sleep
from random import randint
import json

from socketer import Socketer, CONFIG_CLI
from message import Message


class Client(Socketer):

    def __init__(self):
        super().__init__()
        self._name = f"client-{hex(randint(0x100000, 0xffffff))[2:]}"
        self._buf_size = CONFIG_CLI.getint("buf_size")
        self._arr_size_max = CONFIG_CLI.getint('arr_size_max')
        a = [
            1,
            2,
            3,
            3,
            3,
        ]
        self._abs_val_limit = CONFIG_CLI.getint("abs_val_limit")

    def _try_connect_forever(self):
        sock = self._server_socket
        while True:
            try:
                sock.connect((self._server_host, self._server_port))
                return
            except ConnectionRefusedError as err:
                print(err)
                continue

    def make_request_data(self):
        n = self._arr_size_max
        a = self._abs_val_limit
        return [randint(-a, +a) for _ in range(n)]

    def make_request(self):
        data = self.make_request_data()
        return Message(self._name, data)

    # def parse_response(self, resp: bytes):
    #     s = resp.decode(self._encoding)
    #     d = json.loads(s)
    #     return d

    def check_response_data(self, data):
        n = len(data)
        for i in range(1, n):
            if data[i] < data[i - 1]:
                return False
        return True

    def run(self):
        sock = self._server_socket
        self._try_connect_forever()
        while True:
            try:
                req = self.make_request()
                req.send(sock)
                resp = Message.receive(sock)
                print(resp)
                sleep(1.0)
            except KeyboardInterrupt:
                break
            except (ConnectionAbortedError, ConnectionResetError) as err:
                print(err)
                sock.close()
                self._server_socket = Client._create_server_socket()
                sock = self._server_socket
                self._try_connect_forever()
                continue

        sock.close()
