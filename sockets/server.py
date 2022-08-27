import socket
import time
s = socket.socket()
s.bind((socket.gethostname(), 8015))
s.listen(5)
c, adr=s.accept()
print("connection to "+ str(adr)+" established")
##c.send('hello'.encode())
##print(c.recv(1024).decode())
for x in range(1,11):
    print("sending-->",x)
    c.send(str(x).encode())
    msg = c.recv(1024).decode()
    time.sleep(3)
    print("ack-->", msg)
    time.sleep(5)
