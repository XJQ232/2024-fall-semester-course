str1 = ['q','w','e','r','t','y','u','i','o','p']
str2 = ['a','s','d','f','g','h','j','k','l',';']
str3 = ['z','x','c','v','b','n','m',',','.','/']
dire = input()
str4 = input()
if dire == 'R':
    for i in str4:
        if i in str1:
            print(str1[str1.index(i)-1],end='')
        elif i in str2:
            print(str2[str2.index(i)-1],end='')
        else:
            print(str3[str3.index(i)-1],end='')
else:
    for i in str4:
        if i in str1:
            print(str1[str1.index(i)+1],end='')
        elif i in str2:
            print(str2[str2.index(i)+1],end='')
        else:
            print(str3[str3.index(i)+1],end='')
