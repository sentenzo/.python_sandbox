from __future__ import annotations

from socket import *
import json

from socketer import CONFIG_GEN


class Message:

    def __init__(self, sender_name: str, data: list[int]) -> None:
        self.sender_name = sender_name
        self.data = data

    def to_bytes(self):
        d = {"sender": self.sender_name, "data": self.data}
        s = json.dumps(d)
        b = bytes(s, encoding=CONFIG_GEN["encoding"])
        return b

    def send(self, sock: socket):
        sock.send(self.to_bytes())

    @staticmethod
    def from_bytes(b: bytes) -> Message:
        s = b.decode(CONFIG_GEN["encoding"])
        d = json.loads(s)
        return Message(d["sender"], d["data"])

    @staticmethod
    def receive(sock: socket):
        b = b""
        while True:
            data = sock.recv(1024)
            b += data
            if not data:
                break
        return Message.from_bytes(b)

    def __str__(self) -> str:
        repr_data = str(self.data)
        if repr_data > 30:
            repr_data = repr_data[:-4] + " ..."
        return f"{self.sender_name}: {repr_data}"
