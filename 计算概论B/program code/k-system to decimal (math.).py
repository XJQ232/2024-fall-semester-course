l1={'A',"B","C","D","E",'F'}
n,m=input().split()
m=int(m)
len1=len(n)
ans = 0
for i in range(len1):
    if n[i] in l1:
        curr = ord(n[i])-55
    else:
        curr = int(n[i])
    ans += curr*m**(len1-1-i)
print(ans)