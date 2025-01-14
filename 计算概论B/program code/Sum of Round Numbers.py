n = int(input())
str1=0
ans=['']*5
def work(a):
    dig=0
    while a//10 !=0:
        a //=10
        dig+=1
    return dig
for i in range(n):
    str1= int(input())
    total = 0
    curr = work(str1)
    for j in range(curr+1):
        if str1 % 10 !=0:
            total +=1
            ans.append(str(str1 % 10 *10**j) )
        str1=str1//10
    print(total)
    print(' '.join(ans))
    ans.clear()