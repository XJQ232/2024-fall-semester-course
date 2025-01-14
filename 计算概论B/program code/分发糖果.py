ratings = list(map(int, input().split()))
n = len(ratings)


def cmp(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    if a == b:
        return 0


stat = cmp(ratings[0], ratings[1])
step = abs(stat)
total = n + step
step += 1
print(total)
for i in range(1, n-1):
    stat1 = cmp(ratings[i], ratings[i+1])
    if ratings[i+1] == ratings[i]:
        step = 1
        stat = 0
    else:
        if stat1 == stat:
            total += step
            step += 1
        else:
            if stat == -1:
                step = 1
            else:
                total += 1
                step = 2
            stat =stat1
    print(total)
print(total)
