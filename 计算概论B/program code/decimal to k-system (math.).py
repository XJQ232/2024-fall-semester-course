n,m=map(int,input().split()) 
str1 =[]
while n>0:
    curr = n%m
    if curr <= 9:
        str1.append(str(curr))
    if curr == 10:
        str1.append("A")
    if curr == 11:
        str1.append("B")
    if curr == 12:
        str1.append("C")
    if curr == 13:
        str1.append("D")
    if curr == 14:
        str1.append("E")
    if curr == 15:
        str1.append("F")
    n=n//m

str1=str1[::-1]
print(''.join(str1))