from math import sqrt
n,d = map(int,input().split())
curr = 1
while n:
    check = True
    l1=[]
    l2=[]
    for _ in range(n):
        x,y=map(int,input().split())
        if y > d:
            check = False
        else:
            l1.append(x-sqrt(-pow(y,2)+pow(d,2)))
            l2.append(x+sqrt(-pow(y,2)+pow(d,2)))
    if check == False:
        print(f"Case {curr}: -1")
    else:
        l2_sorted = sorted(l2)
        l1_sorted = [x for x,_ in sorted(zip(l1,l2),key=lambda pair:pair[1])]
        total = 1
        ed = l2_sorted[0]
        if n > 1:
            for i in range(1,n):
                if l1_sorted[i] > ed:
                    total += 1
                    ed = l2_sorted[i]
        print(f"Case {curr}: {total}")
    curr += 1
    input()
    n,d = map(int,input().split())