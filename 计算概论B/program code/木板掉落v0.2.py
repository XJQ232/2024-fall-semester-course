H,L,n = map(int,input().split())
v = list(map(int,input().split()))
t=[]
for i in v:
    t.append(L/i)
t.sort()
t1 = t[(n-1)//2]
l = H - 5*pow(t1,2)
print(f"{l:.2f}")