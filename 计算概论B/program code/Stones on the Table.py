a = int(input())
str=input()
curr=str[0]
total = -1
for i in range(a):
    if curr == str[i]:
        total += 1
    else:
        curr = str[i]
print(total)