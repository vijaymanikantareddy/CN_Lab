s = input()
e = input()
msg = input()

ans = ""
ans += s
for ch in msg:
    if ch == s:
        ans += s * 2
    elif ch == e:
        ans += e * 2
    else:
        ans += ch 
ans += e
print(ans)
