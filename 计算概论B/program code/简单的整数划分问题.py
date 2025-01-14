from functools import lru_cache
@lru_cache(maxsize=128)

def work(num,maxn):
    if num <= 1:return 1
    if maxn == 1:return 1
    if num >= maxn:
        return work(num-maxn,maxn)+work(num,maxn-1)
    else:return work(num,num)
while True:
    try:
        n = int(input())
        print(work(n,n))
    except EOFError:
        break