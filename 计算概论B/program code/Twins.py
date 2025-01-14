n = int(input())
l1=list(map(int,input().split()))
l1.sort(reverse=True)
curr=j=0
while 2*curr<= sum(l1):
    curr+=l1[j]
    j+=1
print(j)
