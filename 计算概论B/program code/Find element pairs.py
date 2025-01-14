n = int(input())
l1=list(map(int,input().split()))
m = int(input())
num = 0
for i in range(n):
    if m-l1[i] in l1:
        num+=1
print(num//2)