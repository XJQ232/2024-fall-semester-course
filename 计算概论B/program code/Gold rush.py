n = int(input())
def work(a,b):
    if a < b:return 
    if a== b:return True
    if a % 3:return
    else:
        return work(a//3,b) or work(a*2//3,b)
for _ in range(n):
    a,b = map(int,input().split())
    if work(a,b):print("Yes")
    else:print("No")