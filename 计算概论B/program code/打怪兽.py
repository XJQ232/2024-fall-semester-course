cases = int(input())
for _ in range(cases):
    n,m,b = map(int,input().split())
    dict1 = {}
    time = []
    for __ in range(n):
        t,x = map(int,input().split())
        if t in dict1:
            dict1[t].append(x)
        else:
            dict1[t] = [x]
            time.append(t)
    # print(dict1)
    # print(time)
    time.sort()
    check = False
    for i in time:
        if check:
            break
        dict1[i].sort(reverse=True)
        length = min(m,len(dict1[i]))
        for j in range(length):
            b -= dict1[i][j]
            if b <= 0:
                print(i)
                check = True
                break
    if not check:
        print("alive")