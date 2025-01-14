def work(n,l2,l3,ans):
    if n == 1:
        ans.append(l3+l2)
        return
    for i in range(n):
        l3.append(l2[i])
        work (n-1,l2[0:i]+l2[i+1:],l3,ans)
        l3.pop()
    return ans
s = int(input())
if s == 1:print("1")
else:
    l1=[]
    for i in range(1,s+1):
        l1.append(str(i))
    output = work(s,l1,[],[])
    for i in output:
        print(*i)