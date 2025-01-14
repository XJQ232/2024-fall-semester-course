n = int(input())
total = sum(int(x) for x in input().split() if int(x) % 2==1)
print(total)