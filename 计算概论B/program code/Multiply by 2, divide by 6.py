n = int(input())
for i in range(n):
    m=int(input())
    power3=0
    power2=0
    while m % 3 == 0:
        power3+=1
        m /= 3
    while m % 2 == 0:
        power2 +=1
        m /= 2
    if m!=1 or power2 > power3:
        print("-1")
    else:
        print(2*power3-power2)