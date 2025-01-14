def eight_queen(l1,id,ans):
    if id==8:
        ans.append(l1.copy())
        return
    len1 = len(l1)
    for i in range(8):
        valid = True
        for j in range(len1):
            if i == l1[j]  or abs(id - j) == abs(l1[j] - i):
                valid = False
                break
        if valid:
            l1.append(i)
            eight_queen(l1,id+1,ans)
            l1.pop()
    return

ans=[]
eight_queen([],0,ans)
ans_=[[x+1 for x in i] for i in ans]
n = int(input())
for _ in range(n):
    print(*ans_[int(input())-1],sep='')