n = int(input())
for i in range(n):
    if i == 0:
        print("I hate",end=' ')
    elif i % 2 ==1:
        print("that I love",end=' ')
    elif i % 2 ==0:
        print("that I hate",end=' ')
print("it")

# n = int(input())
# l=[]
# for i in range(n):
#     if i % 2 ==0:
#         l.append("I hate")
#     else:
#         l.append("I love")
# print(" that ".join(l)+' it')