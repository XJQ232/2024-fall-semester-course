n = int(input())
for _ in range(n):
    x = int(input())
    i = 0
    y = x
    while x > 1:
        i += 1
        x //= 2
    print(y*(y+1)//2-pow(2,i+2)+2)