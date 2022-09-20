def xor(x, y):
    ans = ""
    for i in range(1, len(y)):
        if x[i] == y[i]:
            ans += '0'
        else:
            ans += '1'
    return ans
    

def divide(dividend, divisor):
    a = len(divisor)
    temp = dividend[0:a]
    while a < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[a]
        else:
            temp = xor('0'*a, temp) + dividend[a]
        a += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0'*a, temp)
    return temp



#Main of the program.
keys = ['1100000001111','11000000000000101','10001000000100001']

print("Choose the CRC")
print("1. CRC 12")
print("2. CRC 16")
print("3. CRC CCITT")
n = int(input())
send = input("enter Data Sent: ")
rec = input("enter Data Received: ")
key = keys[n - 1]

#encoding sender side
length = len(key)
send1 = send + '0'*(length - 1)
rem = divide(send1, key)

# decoding receiver side
ans = divide(rec, key)
if(ans == '0'*(len(key) - 1)):
    print("no error")
else:
    print("frame error")
