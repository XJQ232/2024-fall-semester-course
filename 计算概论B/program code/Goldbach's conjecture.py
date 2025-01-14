import math
def prime(a):
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

a = int(input())
if a<6 or a % 2 !=0:
    print('Error!')
else:
    for i in range(3,(a+2)//2,2):
        if prime(i)==True and prime(a-i)==True:
            print(a,'=',i,'+',a-i,sep='')

