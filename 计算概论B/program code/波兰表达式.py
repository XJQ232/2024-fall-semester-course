# str1 = {'+','-','*','/'}

# def check (a):
#     if a in str1:return False
#     else:return True
    
# def work2(a,b,c):
#     if c=='+':
#         return a+b
#     if c=='-':
#         return a-b
#     if c=='*':
#         return a*b
#     if c=='/':
#         return a/b
# def work(arr):
#     # print(arr)
#     len1 = len(arr)
#     if len1 == 1:
#         if check(arr[0]):
#             return arr[0]
#         else:
#             print("False")
#     for i in range(len1):
#         if arr[i] in str1:
#             # print(i)
#             # print(l1[i+1],l1[i+2])
#             if check(l1[i+1]) and check(l1[i+2]):
#                 # print(i)
#                 arr[i] = work2(arr[i+1],arr[i+2],arr[i])
#                 # print(arr)
#                 arr.pop(i+1)
#                 arr.pop(i+1)
#                 # print(arr)
#                 return work(arr)

# l1 = list(input().split())
# for i in range(len(l1)):
#     if check(l1[i]):
#         l1[i] = float(l1[i])
# ans = work(l1)
# ans = format(ans,'.6f')
# print(ans)

# import operator
# op= {'+':operator.add}
# l1 = input().split()
# print(op[l1[1]](float(l1[0]),float(l1[2])))

l1 = input().split()
len1 = len(l1)
stack = []
for i in reversed(range(len1)):
    if l1[i][0].isdecimal():
        stack.append(l1[i])
    else:
        x=stack.pop()
        y=stack.pop()
        z = str(eval(x+l1[i]+y))
        stack.append(z)
print('6f'%float(stack[0]))