str1 = input()
curr=1
for i in range(1,len(str1)):
    if str1[i]==str[i-1]:
        curr += 1
    else:
        curr =1
    if curr == 7:
        print("YES")
        exit(0)
print("NO")