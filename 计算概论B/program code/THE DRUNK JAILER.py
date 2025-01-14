n = int(input())
l1=[1,4,9,16,25,36,49,64,81,100,101]
for _ in range(n):
    m = int(input())
    for i in range(10):
        if l1[i] <= m and m<l1[i+1]:
            print(i+1)
