str1 = input().lower()
curr = str1[0]
total = 0
for i in str1:
    if i == curr:
        total+=1
    else:
        print(f'({curr},{total})',end='')
        total = 1
        curr = i
print(f'({curr},{total})')