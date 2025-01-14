def check(a):
    hund=a//100
    ten=a//10 %10
    one=a%10
    if hund**3+ten**3+one**3 == a:
        return True
m,n = map(int,input().split())
num=0
for i in range(m,n+1):
    if check(i):
        num+=1
        if num !=1:
            print(' ',end='')
            print(i,end='')
        else:
            print(i,end='')
if num == 0:
    print("NO")