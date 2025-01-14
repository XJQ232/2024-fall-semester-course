n = int(input())
for _  in range(n):
    s,len1= int(input()),int(input())
    l1 = list(map(int,input().split()))
    dict1 = {}
    for i in l1:
        dict1[i]=l1.count(i)
    len2= int(input())
    l2 = list(map(int,input().split()))
    dict2 = {}
    for i in l2:
        dict2[i]=l2.count(i)
    ans = 0
    for i in dict1:
        if s-i in dict2:
            ans += dict1[i]*dict2[s-i]
    print(ans)