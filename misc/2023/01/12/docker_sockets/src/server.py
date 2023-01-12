from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 8901))
sock.listen(1)
while True:
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(repr(data))
        conn.sendall(data)
    conn.close()
