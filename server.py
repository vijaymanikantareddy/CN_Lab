import socket
import time
import random
s=socket.socket()
s.bind(("localhost", 8020))
s.listen(5)
c, adr = s.accept()
print("connection to " + str(adr) + " established")
a=int(input("enter total number of frames"))
x = 0
print("sending -->", x)
c.send(str(x).encode())
while( a > 1 ):
    timer = 5
    t=random.randint(1,7)
    msg = c.recv(1).decode()
    if( timer > t):
        time.sleep(3)
        print("ack-->", msg)
        x=int(msg)
        print("sending -->", str(x))
        c.send(str(x).encode())
    else:
        time.sleep(3)
        print("timeout")
        print("sending again-->", x)
        c.send(str(x).encode())
        a=a+1
    a = a-1
