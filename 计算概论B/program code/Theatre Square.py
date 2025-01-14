str = input().split(' ')
if int(str[0]) % int(str[2]) == 0:
    n= int(str[0])//int(str[2])
else:
    n= int(str[0])//int(str[2])+1
if int(str[1]) % int(str[2]) == 0:
    m= int(str[1])//int(str[2])
else:
    m= int(str[1])//int(str[2])+1
print(n*m)
