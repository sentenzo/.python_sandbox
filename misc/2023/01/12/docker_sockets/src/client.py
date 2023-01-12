from time import sleep

from socketer import Socketer, CONFIG_CLI


class Client(Socketer):
    def __init__(self):
        super().__init__()
        self._buf_size = CONFIG_CLI.getint("buf_size")

    def _try_connect_forever(self):
        sock = self._server_socket
        while True:
            try:
                sock.connect((self._server_host, self._server_port))
                return
            except ConnectionRefusedError as err:
                print(err)
                continue

    def run(self):
        sock = self._server_socket
        self._try_connect_forever()
        while True:
            try:
                sock.send(b"Hello!\n")
                data = sock.recv(1024)
                print(repr(data))
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
