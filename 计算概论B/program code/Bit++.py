n = int(input())
sum = 0
str=''
for i in range(n):
    str=input()
    if '+' in str:
        sum+=1
    else:
        sum-=1
print(sum) 