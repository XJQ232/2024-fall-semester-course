from math import sqrt
n = int(input())
for i in range(n):
    a = int(input())
    while a % 2 == 0:
        a /= 2
    if a!=1:
        print("YES")
    else:
        print("NO")
