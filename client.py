import socket
import time
s=socket.socket()
s.connect(("localhost", 8020))
while(1):
    msg=s.recv(1).decode()
    print("Received --> ", msg)
    x=int(msg)
    if(x==0):
        x=x+1
        s.send(str(x).encode())
    else:
        x=x-1
        s.send(str(x).encode())
