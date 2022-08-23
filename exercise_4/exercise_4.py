li = list(map(int,input().split()))
rec = list(map(int,input().split()))

li = li[::-1]

li = [0,0] + li[0:1] + [0] + li[1:4] + [0] + li[4:]

li[0] = (li[2] + li[4] + li[6] + li[8] + li[10]) % 2
li[1] = (li[2] + li[5] + li[6] + li[9] + li[10]) % 2
li[3] = (li[4] + li[5] + li[6]) % 2
li[7] = (li[8] + li[9] + li[10]) % 2

li = li[::-1]

rec = rec[::-1]
r1 = (rec[0] + rec[2] + rec[4] + rec[6] + rec[8] + rec[10]) % 2
r2 = (rec[1] + rec[2] + rec[5] + rec[6] + rec[9] + rec[10]) % 2
r3 = (rec[3] + rec[4] + rec[5] + rec[6]) % 2
r4 = (rec[7] + rec[8] + rec[9] + rec[10]) % 2

bit = str(r4) + str(r3) + str(r2) + str(r1)
bit = int(bit,2)
if bit :
    print(bit)
else:
    print("no error")

