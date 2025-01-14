str1 = input()
l1=[1]*len(str1)
max1 = 1
for i in range(1,len(str1)):
    if str1[i] != str1[i-1]:
        l1[i] = l1[i-1]+1
        if l1[i]>max1:
            max1=l1[i]
print(max1)