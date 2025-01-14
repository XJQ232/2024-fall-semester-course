a =int( input())
b=0
str =input().split(' ')
for i in range(a):
    b+=float(str[i])
print(b/a)