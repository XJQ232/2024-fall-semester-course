str = input().split(' ')
n = int(str[0]);m= int(str[1])
s= n
while(n-m>=0):
    n = n-m+1
    s+=1
print(s)