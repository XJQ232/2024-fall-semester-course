n = int(input())
l1 = list(map(int,input().split()))
sum1 = sum(l1)
if sum1 % 3:
    print("0")
else:
    if sum1:
        sum1 = sum1//3
        l_1 = []
        total = 0
        curr = 0
        step2 = 0
        step1 = 1
        for i in range(n):
            curr += l1[i]
            if curr == sum1 and l1[i]:
                l_1.append(1)
            if curr == sum1 and not l1[i]:
                l_1.append(2)
            elif curr == sum1*2:
                l_1.append(2)
                step2 += 1
        for i in l_1:
            if i == 1:
                total += step1 * step2
                step1 += 1
            if i == 2:
                step2 -= 1
        print(total)
    else:
        curr = 0
        num = 0
        for i in range(n):
            curr += l1[i]
            if not curr:
                num += 1
        num -= 1
        print(num*(num-1)//2)