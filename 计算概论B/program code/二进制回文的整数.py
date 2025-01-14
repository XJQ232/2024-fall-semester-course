str1 = bin(int(input()))[2:]
str2 =''
for i in reversed(range(len(str1))):
    str2 += str1[i]
# print(str1,str2)
print("Yes" if str1 == str2 else "No")