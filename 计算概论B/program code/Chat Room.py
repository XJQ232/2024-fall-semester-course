word = input().lower()
sum=0
for i in word:
    if i =='h' and sum == 0:
        sum+=1
    if i=='l' and (sum == 2 or sum ==3):
        sum+=1
    if i=='e' and sum == 1:
        sum +=1
    if i=='o' and sum ==4:
        sum +=1
    else :
        sum +=0
if sum == 5:
    print("YES")
else:
    print("NO")