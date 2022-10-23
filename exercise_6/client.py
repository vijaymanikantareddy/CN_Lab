import socket
import time
s = socket.socket()
s.connect(("localhost", 1450))
while 1:
    msg = s.recv(2).decode()
    print("Received --> ", int(msg))
    s.send(str(msg).encode())
    time.sleep(1)
