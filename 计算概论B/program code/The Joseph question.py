while True:
    n,m = map(int,input().split())
    if not n:
        break
    check = list(range(n))
    m %= n
    left = n
    curr = m-1
    while n > 1:
        check.pop(curr)
        n -= 1
        curr += m-1
        curr %= n
    for item in check:
        print(item+1)