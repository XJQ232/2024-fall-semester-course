from math import isqrt
def seive_of_Euler(limit):
    isprime=[0]*(limit+1)
    isprime[0]=isprime[1]=1
    prime=[]
    for i in range(limit+1):
        if isprime[i] == 0:
            prime.append(i)
        for j in prime:
            if i*j >limit:
                break
            isprime[i*j]=1
            if i%j == 0:break
    return prime
n = int(input())
l1 = list(map(int,input().split()))
m=isqrt(max(l1))+1
prime=seive_of_Euler(m)
ans=set(p*p for p in prime)
for i in l1:
    if i in ans:
        print("YES")
    else:
        print("NO")