n = int(input())%26
str1 = input()
for i in str1:
    if ord(i) in range(65,91):
        if (ord(i)-n-64)%26+64 != 64:
            print(chr((ord(i)-n-64)%26+64),end='')
        else:
            print('Z',end='')
    if ord(i) in range(97,123):
        if (ord(i)-n-96)%26+96 != 96:
            print(chr((ord(i)-n-96)%26+96),end='')
        else:
            print('z',end='')