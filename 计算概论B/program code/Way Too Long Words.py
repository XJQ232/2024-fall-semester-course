n = int(input())
for i in range(n):
    str1 = input()
    if len(str1)<=10:
        print(str1)
    else:
        print(f'{str1[0]}{len(str1)-2}{str1[-1]}')