n = int(input())
queue = list(map(int,input().split()))
queue.sort()
total = 0
time = 0
check = [True]*n
for i in range(n):
    if time <= queue[i] and check[i]:
        check[i] = False
        total += 1
        time += queue[i]
    else:
        continue
print(total)