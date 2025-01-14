money = int(input())
l1=list(map(int,input().split()))
l1.sort()
total = 0
i = 0
j = -1
check = [True]*len(l1)
for i in range(len(l1)):
    if money >= l1[i]:
            money -= l1[i]
            total += 1
    else:
        
        for j in range(-1,-len(l1),-1):
            if i == j:
                if money > l1[i]:
                    total +1
                break
            if l1[j] + money >= l1[i] and check[j] and total > 0:
                money = money+l1[j] - l1[i]
                check[j] = False
                break
print(total)