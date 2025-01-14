a=[0]*2
def work(x,y):
    if x % y == 0:
        print(y)
    else:
        work(y,x % y)
while(True):
    try:
        a=list(map(int,input().split()))
        work(max(a[0],a[1]),min(a[0],a[1]))
    except EOFError:
        break
