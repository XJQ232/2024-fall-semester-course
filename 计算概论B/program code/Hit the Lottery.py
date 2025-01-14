a=[1,5,10,20,100]
n=int(input())
sum = 0
a.sort(reverse=True)
for i in a:
    if n > 0:
        sum += n//i
        n -= n//i * i
    else:
        break
print(sum)