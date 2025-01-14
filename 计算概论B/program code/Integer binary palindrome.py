n= int(input())
str1 = bin(n)
for i in range(2,len(str1)):
    if str1[i] != str1[len(str1)-i+1]:
        print("No")
        exit(0)
print("Yes")