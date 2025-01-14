# l1 =list(input())
# ans = l1[0]
# max1 = 0
# len1 = len(l1)
# for i in range(len1):
#     stack = [(i,i,1)]
#     step = 1
#     while i+step < len1 and l1[i] == l1[i+step]:
#         stack.pop()
#         stack.append((i,i+step,1+step))
#         step += 1
#     i = i+step  -1
#     while stack:
        
#         x,y,k = stack.pop()
#         if k > max1:
#             max1 = k
#             ans = ''.join(l1[x:y+1])
#         if x -1 >=0 and y+1 < len1 and l1[x-1] == l1[y+1]:
#             stack.append((x-1,y+1,k+2))
# print(ans)

l1 =list(input())
def work(s,ide):
    
s= l1[0]
ans = l1[0]
max1 = 0
len1 = len(l1)
dp=[1]*(2*len1-1)
work(s,1,1)

print(ans)