n = int( input())
l1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
l2=['1','0','X','9','8','7','6','5','4','3','2']
for _ in range(n):
    str1 = input()
    sum_ = 0
    for i in range(17):
        sum_ += int(str1[i])*l1[i]
    sum_ %= 11
    if l2[sum_] == str1[17]:
        print("YES")
    else:
        print("NO")
    