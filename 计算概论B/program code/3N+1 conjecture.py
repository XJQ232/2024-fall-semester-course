n = int(input())
num = 0
while n!=1:
    if n%2 == 0:
        n//=2
        num+=1
    else:
        n=(n*3+1)//2
        num+=1
print(num)