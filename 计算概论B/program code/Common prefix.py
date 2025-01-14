n = int(input())
str1=[]
ans=[]
for i in range(n):
    str1.append(input())
curr = str1[0][0]
len1 =len(str1[0])
now = True
for i in range(len1):
    curr = str1[0][i]
    if not now:
        break
    for j in range(n):
        if i == len(str1[j]):
            print(''.join(ans))
            exit()
        if not(str1[j][i] == curr): now=False;break
    if now == True:ans.append(curr)
print(''.join(ans))