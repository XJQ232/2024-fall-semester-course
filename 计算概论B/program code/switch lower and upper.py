str1 = input()
for i in str1:
    if i.isupper():
        print(i.lower(),end='')
    elif i.islower():
        print(i.upper(),end='')
    else:
        print(i,end='')