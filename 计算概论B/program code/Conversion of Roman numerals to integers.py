l1 = ['I','V',"X","C","M","L",'D']
str1 = input()
if str1[0] in l1:
    len1 = len(str1)
    total = 0
    for i in range(len1):
        if i < len1 - 1:
            if str1[i] == 'I' and (str1[i+1] == 'X' or str1[i+1] == 'V'):total -= 1;continue
            if str1[i] == 'X' and (str1[i+1] == 'L' or str1[i+1] == 'C'):total -= 10;continue
            if str1[i] == 'C' and (str1[i+1] == 'D' or str1[i+1] == 'M'):total -= 100;continue
            else:
                if str1[i] == 'I':total += 1
                if str1[i] == 'V':total += 5
                if str1[i] == "X":total += 10
                if str1[i] == 'L':total += 50
                if str1[i] == 'C':total += 100
                if str1[i] == 'D':total += 500
                if str1[i] == 'M':total += 1000
        else:
            if str1[i] == 'I':total += 1
            if str1[i] == 'V':total += 5
            if str1[i] == "X":total += 10
            if str1[i] == 'L':total += 50
            if str1[i] == 'C':total += 100
            if str1[i] == 'D':total += 500
            if str1[i] == 'M':total += 1000
    print(total)
else:
    n = int(str1)
    while n - 1000 >= 0:
        print('M',end = '')
        n-=1000
    if n - 900 >= 0:
        print('CM',end='')
        n-=900
    if n - 500 >= 0:
        print('D',end='')
        n -= 500
    if n - 400 >= 0:
        print('CD',end='')
        n-=400
    while n -100 >= 0:
        print("C",end='')
        n-=100
    if n -90 >= 0:
        print("XC",end='')
        n-=90
    if n-50 >= 0:
        print("L",end='')
        n-=50
    if n-40 >= 0:
        print("XL",end='')
        n-=40
    while n-10 >=0:
        print("X",end='')
        n-=10
    if n-9>=0:
        print("IX",end='')
        n-=9
    if n-5>=0:
        print("V",end='')
        n-=5
    if n-4>=0:
        print("IV",end='')
        n-=4
    while(n-1>=0):
        print("I",end='')
        n-=1
    print()