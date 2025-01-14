import math

def check(a):
    a=str(a)
    for i in a:
        if i!='4' and i!='7':
            return False
    return True

n=int(input())
if check(n) == True:
    print("YES")
else:
    for i in range(n):
        if check(i) == True:
            if n % i ==0:
                print("YES")
                exit(0)
    print("NO")
