str1 = input()
num =[0]*len(str1)
for i in range(len(str1)-1):
    num[i+1] = num[i] + (str1[i] == str1[i+1])
n = int(input())
for _ in range(n):
    l,r=map(int,input().split())
    ans = num[r-1]-num[l-1]
    print(ans)