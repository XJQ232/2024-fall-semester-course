str=input().split(' ')
a = int( str[0] )
b= int ( str[1] )
if a*b % 2 ==0:
    print(a*b//2)
else:
    print((a*b-1)//2)
