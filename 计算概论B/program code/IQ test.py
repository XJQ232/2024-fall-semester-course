n = int(input())
l1=list(map(int,input().split()))
e=0
o=0
for i in l1:
    if i % 2==0:
        e+=1
    else:
        o+=1
for i in range(n):
    if l1[i]%2==0 and o>1:
        print(i+1)
    if l1[i]%2==1 and e>1:
        print(i+1)

# x = int(input())
# arr = [int(q) for q in input().split()]
# evens = 0
# odds = 0
# for i in arr:
#   if i%2 == 0:
#     evens+=1
#   else:
#     odds+=1
# if evens > odds:
#   for i in arr:
#     if i%2 == 1:
#       print(arr.index(i)+1)
#       break
# else:
#   for i in arr:
#     if i%2 == 0:
#       print(arr.index(i)+1)
#       break