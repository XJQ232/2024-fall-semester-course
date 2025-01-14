testnumber = int(input())
for _ in range(testnumber):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = [l1[0]]
    for i in range(1, n):
        l2.append(l2[i-1]+l1[i])
    dict1 = {}
    for i in range(n):
        if l2[i] in dict1:
            dict1[l2[i]].append(i)
        else:
            dict1[l2[i]] = [i]
    star1 = []
    end1 = []
    total = 0
    check = False
    for i in dict1:
        if len(dict1[i]) > 1:
            for j in range(len(dict1[i])-1):
                star1.append(dict1[i][j])
                end1.append(dict1[i][j+1])
            check = True
    if not check:
        if 0 not in dict1:
            print("0")
            continue
        else:
            print("1")
            continue
    else:
        star1_sorted = [x for x, _ in sorted(
            zip(star1, end1), key=lambda pair: pair[1])]
        end1_sorted = [x for _, x in sorted(
            zip(star1, end1), key=lambda pair: pair[1])]
        curr = 0
        total = 1
        for i in range(1, len(end1_sorted)):
            if star1_sorted[i] > end1_sorted[curr]:
                curr = i
                total += 1
        if l1[0] == 0:
            total += 1
        if n > 1 and l1[-1] == 0 and curr != len(end1_sorted)-1:
            total += 1
        print(total)
