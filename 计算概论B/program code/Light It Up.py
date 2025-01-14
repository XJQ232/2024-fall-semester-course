n, M = map(int, input().split())
l1 = list(map(int, input().split()))
l1.append(M)
if n == 1:
    print(max(l1[0], M-1))
else:
    l_odd = [l1[0]]
    l_even = [0]
    step = 1
    for i in range(n):
        if step % 2:
            l_even.append(l_even[-1]+l1[i+1]-l1[i])
        else:
            l_odd.append(l_odd[-1]+l1[i+1]-l1[i])
        step += 1
    len1 = len(l_odd)
    max1 = 0
    for i in range(len1-(n+1)%2):
        max1 = max(max1,l_odd[i]+l_even[-1]-l_even[i]-1)
    max1 = max(max1,l_odd[-1])
    print(max1)