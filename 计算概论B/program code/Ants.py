import bisect
testnumber = int(input())
for _ in range(testnumber):
    length,n = map(int,input().split())
    l1=sorted(list(map(int,input().split())))
    min1 = 99999
    for i in l1:
        if abs(i-length/2) < min1:
            min1 = abs(i-length/2)
            ans1 = min(i,length-i)
    ans2 = max(l1[0],length-l1[0],l1[-1],length-l1[-1])
    print(ans1,ans2)