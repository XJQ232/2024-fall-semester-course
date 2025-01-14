str1 = list(input().lower())
str2=''
vowvel='aeiouy'
for i in str1:
    if i in vowvel:
        del(i)
    else:
        str2=str2+'.'+i
print(str2)