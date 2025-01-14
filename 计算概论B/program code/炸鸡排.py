def  work(sum1,arr,num):
    temp = sum1 / num
    if arr[0] > temp:
        return work(sum1-arr[0],arr[1:],num-1)
    return temp
n,k = map(int,input().split())
l1 = sorted(list(map(int,input().split())),reverse=True)
s1 = sum(l1)
ans = format(work(s1,l1,k),'.3f')
print(ans)