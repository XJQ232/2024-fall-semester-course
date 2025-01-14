str = list(map(int,input().split('+')))
if len(str) == 1:
    print(str[0])
else:
    a=str.count(1)
    b=str.count(2)
    c=str.count(3)
    s=a+b+c
    for i in range(s):
        if i < a:
            print('1',end='')
        elif i < a+b:
            print('2',end='')
        elif i <a+b+c:
            print('3',end='')
        if i<s-1:
            print('+',end='')