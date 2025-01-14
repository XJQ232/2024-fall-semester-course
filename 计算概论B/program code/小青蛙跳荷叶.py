n = int(input())
x=1;y=1
for i in  range(n-1):
    y,x= x,x+y
print(x)