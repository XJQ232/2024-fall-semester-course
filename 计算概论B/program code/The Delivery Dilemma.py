testnumber = int(input())
for _ in range(testnumber):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l2_sorted=[x for _,x in sorted(zip(l1,l2),key=lambda pair:pair[0],reverse=True)]
    l1_sorted=sorted(l1,reverse=True)
    l1_sorted.append(0)
    curr = 0
    min1 = l1_sorted[0]
    for i in range(n):
        curr += l2_sorted[i]
        step = max(l1_sorted[i+1],curr)
        if min1 > step:
            min1 = step
    print(min1)