def work(a):
    prime=[0]*(a+1)
    prime[0]=1
    prime[1]=1
    l1=[]
    num = 0
    for i in range(a+1):
        if not prime[i]:l1.append(i);num+=1
        for j in range(num):
            if i*l1[j]<=a:
                prime[i*l1[j]]=1
            if i%l1[j] == 0:
                break
    return set(l1)
n = int(input())
m=(n-1)//2+1
prime=work(n)
while True:
    if m in prime and (n-m) in prime:
        print(m*(n-m))
        exit()
    else:
        m-=1