def work(n,l2,l3,ans):
    if n == 1:
        ans.add(tuple(l2+l3))
        return
    for i in range(n):
        l3.append(l2[i])
        work (n-1,l2[0:i]+l2[i+1:],l3,ans)
        l3.pop()
    return ans
s = int(input())
l1=sorted(list(map(int,input().split())))
if s ==1 :
    print(*l1)
else:
    temp = set()
    output = sorted(work(s,l1,[],temp))
    for i in output:
        print(' '.join(map(str,i)))