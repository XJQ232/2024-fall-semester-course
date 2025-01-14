n= int(input())
for i in range(n):
    m = int(input())
    if 360 % (180-m) == 0:
        print("YES")
    else:
        print("NO")