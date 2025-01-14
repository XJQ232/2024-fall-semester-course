from math import ceil
n = int(input())
while n!=0:
    min = 999999999
    for i in range(n):
        v,t=map(int,input().split())
        if t>=0 and ceil(16200/v+t)<min:
            min = ceil(16200/v+t)
    print(min)
    n = int(input())