l1,l2=input(),input()
len1 = len(l1)
len2 = len(l2)
l1=list(l1)
l1.reverse()
l2=list(l2)
l2.reverse()
curr = 0
c=[]
m = max(len1,len2)
n = min(len1,len2)
if len1 > len2:
    for i in range(n ,len1):
        l2.append('0')
elif len1 < len2:
    for i in range(n,len2):
        l1.append('0')
for i in range(m):
    a=int(l1[i])
    b=int(l2[i])
    c.append(str((curr + a+b)%10))
    curr = (curr+a+b)//10
if curr == 1:
    c.append('1')
head = True
step = 0
while head:
    if len(c) == 1:
        break
    if c[-1] == '0' and head:
        c.pop(-1)
    else:
        head = False
c.reverse()
print(''.join(c))