from socketer import Socketer, CONFIG_SVR


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
