n = int(input())
for i in range(n):
    if i == 0 or i == n-1:
        str1='*'*(i+1)
        print(str1)
    else:
        str1="*"+' '*(i-1)+'*'
        print(str1)