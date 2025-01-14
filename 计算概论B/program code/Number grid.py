def work(a,b,c):
    global max1
    if (a+b) % 2 == 0 and (b+c) % 3 == 0 and (a+b+c) % 5 == 0 and max1 < a+b+c:
        max1 = a+b+c
    else:
        if a>=1:
            work(a-1,b,c)
        if b>=1:
            work(a,b-1,c)
        if c>=1:
            work(a,b,c-1)
n=int(input())
max1 = 0
work(n,n,n)
print(max1)