from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 8901))
sock.send(b"Hello!\n")
data = sock.recv(1024)
sock.close()
print(repr(data))
