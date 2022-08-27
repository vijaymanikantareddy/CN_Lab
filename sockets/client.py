import socket
import time
s = socket.socket()
s.connect((socket.gethostname(), 8015))
## s.send("hai".encode())
##msg = s.recv(1024).decode()
##print(msg)
for x in range(1, 11):
    msg = s.recv(1024).decode()
    time.sleep(5)
    print("Received-->", msg)
    s.send(str(x+1).encode())
