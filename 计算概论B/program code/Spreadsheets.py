testnumber = int(input())
def number_to_character(n):
    l1=[]
    while n>0:
        if n%26:
            l1.append(n%26)
            n = n//26
        else:
            l1.append(26)
            n = n//26 - 1
    l1=l1[::-1]
    ans= ''
    for i in l1:
        ans += chr(i+64)
    return ans
def character_to_number(str0):
    ans = 0
    for i in str0:
        ans *= 26
        ans += ord(i)-64
    return str(ans)
for _ in range(testnumber):
    str1 = input()
    typenumber = 0
    curr = str1[0].isdigit()
    for i in str1:
        if i.isdigit() != curr:
            typenumber += 1
            curr = i.isdigit()
    if typenumber == 3:
        id1 = str1.find('C')
        row = ''
        column = ''
        for i in range(1,id1):
            row += str1[i]
        for i in range(id1+1,len(str1)):
            column += str1[i]
        columnumber = int(column)
        print(number_to_character(columnumber) + row)
    else:
        row=''
        column=''
        for i in str1:
            if i.isdigit():
                row += i
            else:
                column += i
        print('R'+row+'C'+character_to_number(column))