n,d=map(int,input().split())
l0=[]
l1=[]
l2=[]
l3=[]
max1 = 0
min1 = 999999999
max2 = 0
min2 = 999999999
for _ in range(n):
    l0.append(int(input()))
l2=l0.copy()
k = len(l2)
while k > 0:
    l1.clear()
    l3.clear()
    max1=l2[0]
    min1=l2[0]
    max2=l2[0]
    min2=l2[0]
    check = True
    for i in range(k):
        if not(abs(min1-l2[i])>d or abs(l2[i] - max1) > d):
            if check:
                l1.append(l2[i])
                l3.append(i)
                if min1 >= l2[i]:
                    min1 = l2[i]
                if max1 <= l2[i]:  
                    max1 = l2[i]
            else:
                if not(abs(min2-l2[i])>d or abs(l2[i] - max2) > d):
                    l1.append(l2[i])
                    l3.append(i)
        else:
            check = False
            if min2 >= l2[i]: min2 = l2[i]
            if max2 <= l2[i]: max2 = l2[i]

    l1.sort()
    for i in l1:
        print(i)
    for i in sorted(l3,reverse=True):
        l2.pop(i)
    k = len(l2)