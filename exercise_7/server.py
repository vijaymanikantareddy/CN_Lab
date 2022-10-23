import socket
import random
import time
s = socket.socket()
s.bind(("localhost", 8038))
s.listen(5)
c, adr = s.accept()
print(str(adr))
n = int(input("Enter number of frames: "))
N = int(input("Enter window size: "))
seq = 1  # is used to keep track of the window starting
frame = 1  # frame to send starts with 1

# send first N window size frames
for i in range(N):
    print('Frames sent ->', frame)
    c.send(str(frame).encode())
    frame += 1
    time.sleep(2)

timer = 5

# will start with acknowledgement frame of 1
while frame <= n:
    t = random.randint(1, 7)
    msg = c.recv(1).decode()
    msg = int(msg)
    print("Frame ", msg)
    if (timer > t):  # if the timer is greater than random number be consider it as ack
        print("acknowledgement received")
        print('Frames sent ->', str(frame))
        # we will send next frame
        c.send(str(frame).encode())
        seq += 1
        frame += 1
        time.sleep(2)
    else:  
        # if timer is less than the random number we consider as not received ack
        print('acknowledgement not received')
        # we will again send the frames from window starting i.e seq
        print('Frames sent ->', seq)
        c.send(str(seq).encode())
        time.sleep(2)
