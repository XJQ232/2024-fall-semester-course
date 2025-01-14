l1=['A','B','C']
def work(n,a,b,c):
    str1 = l1[a]+'->'+l1[b]+'\n'
    if n==1:
        return str1
    return work(n-1,a,c,b) + str1 + work(n-1,c,b,a)
n = int(input())
a = 1 << n
print(a-1)
ans = work (n,0,2,1)
print(ans)