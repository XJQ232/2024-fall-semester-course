numberoftest = int(input())
for _ in range(numberoftest):
    total = int(input())
    step = 1
    ans = 0
    while total > 0:
        if total % 4 == 2 or total == 4:
            curr = total // 2
        else:
            curr = 1
        if step % 2:
            ans += curr
        step += 1
        total -= curr
    print(ans)
