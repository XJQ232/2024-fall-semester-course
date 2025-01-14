n = int(input())
curr=''
sum=0
for i in range(n+1):
    curr=str(i)
    if not('7' in curr or int(curr)%7 ==0):
        sum+=int(curr)**2
print(sum)