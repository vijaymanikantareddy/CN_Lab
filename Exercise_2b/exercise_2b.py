n = int(input())
s = input()
c = 0
res = ""
for i in s:
    if i == '1' and c < 5:
        res += '1'
        c += 1
    elif i == ' ':
        pass
    else :
        res += i
        c = 0
    if c == 5:
        res += '0'
        c = 0
print(res)
