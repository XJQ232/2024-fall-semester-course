n = int(input())
l1 = list(map(int, input().split()))
for i in range(n):
    l1[i] -= 1
l2 = [0]*n
for i in range(n):
    l2[l1[i]-1] = i+1
str1 = input()


def work(str1):
    ans = ''
    for i in range(n):
        ans += str1[l2[i]-1]
    return ans



while str1 != '0':
    num = ''
    text = ''
    output=''
    check = True 
    for i in str1:
        if check:
            if i.isdigit():
                num += i
            else:
                check = False
        else:
            text += i
    if len(text) < n:
        text = text + ' '*(n-len(text))
    num = int(num)
    for i in range(n):
        for j in range(zhouqi[i]):
            output+=work()
    print(text)
    str1 = input()
input()