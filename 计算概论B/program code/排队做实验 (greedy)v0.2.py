n = int(input())
l1 = list(map(int, input().split()))
if n == 1:
    print('1')
    print('0.00')

else:
    l2 = sorted(range(1, n+1), key=lambda x: l1[x-1])
    l1.sort()
    sum1 = 0
    for i in range(n):
        sum1 += (n-i-1)*l1[i]
    average = format(sum1/n, '.2f')
    print(*l2)
    print(average)
