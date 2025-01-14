n = int(input())
boy = list(map(int,input().split()))
m = int(input())
girl = list(map(int,input().split()))
boy.sort()
girl.sort()
step1 = 0;ans = 0;step2 = 0
while step1 < n and step2 < m:
    if abs(girl[step2]-boy[step1])<=1:
        ans += 1
        step1 += 1
        step2 += 1
    elif girl[step2] > boy[step1]:
        step1 += 1
    elif girl[step2] < boy[step1]:
        step2 += 1
print(ans)
