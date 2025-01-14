n = int(input())
def work(a):
    i=0
    while(a>1):
        i+=1
        a//=2
    return i
for i in range(n):
    m=int(input())
    power=work(m)
    print(m*(m+1)//2-2**(power+2)+2)