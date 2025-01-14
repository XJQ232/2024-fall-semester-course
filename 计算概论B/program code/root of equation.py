import math
n = int(input())
a=b=c=d=0
for i in range(n):
    a,b,c=(map(float,input().split()))
    d=b**2 - 4*a*c
    if b==0:
        b=-b
    if  d == 0:
        x=format(-b/(2*a),'.5f')
        print(f'x1=x2={x}')
    elif d>0:
        x1=format((-b+math.sqrt(d))/(2*a),".5f")
        x2=format((-b-math.sqrt(d))/(2*a),'.5f')
        print(f'x1={x1};x2={x2}')
    elif d<0:
        x11=(format(-b/(2*a),'.5f'))
        x12=(format(math.sqrt(-d)/(2*a),'.5f'))
        print(f'x1={x11}+{x12}i;x2={x11}-{x12}i')
