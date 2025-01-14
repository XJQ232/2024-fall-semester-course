from math import isqrt
n = int(input())
count = 0
i = 2
while n>1:
    if n % i == 0:
        if n % i**2 == 0:
            print("0")
            exit()
        n =n // i
        count += 1
    else:
        i += 1
print("-1" if count % 2 else "1")