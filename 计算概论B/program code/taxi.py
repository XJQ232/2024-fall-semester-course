n = int(input())
l1=sorted(list(map(int,input().split())))
dic1={}
check = [False] * 5
set1 = set(l1)
for i in set1:
    dic1[i]=l1.count(i)
    check[i]=True
total = 0;spare = 0
if check[4]:
    total += dic1[4]
if check[3]:
    total += dic1[3]
    spare += dic1[3]
if check[2]:
    total += (dic1[2]-1)//2 + 1
    spare += 2*(dic1[2] % 2)
if check[1]:
    if spare < dic1[1]:
        total += (dic1[1]-spare-1)//4+1
print(total)
