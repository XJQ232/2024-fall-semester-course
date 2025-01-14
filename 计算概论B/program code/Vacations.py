# import sys
# sys.setrecursionlimit(1 << 30)
# n = int(input())
# l1 = list(map(int, input().split()))
# l2 = []
# total = 0


# def work(arr, ans,state):
#     for i in range(len(arr)):
#         if not arr[i]:
#             ans += 1
#             state = 0
#         else:
#             if i == len(arr) - 1:
#                 return ans
#             else:
#                 if arr[i] == 3:
#                     if not state:
#                         temp1 = work([1]+arr[i+1:], ans,1)
#                         temp2 = work([2]+arr[i+1:], ans,2)
#                         if temp1 <= temp2:
#                             arr[i] = 1
#                             ans = temp1
#                         else:
#                             arr[i] = 2
#                             ans = temp2
#                     else:arr[i] = 3- state
#                     state = arr[i]
#                 else:
#                     if i == 0:
#                         state = arr[i]
#                     else:
#                         if arr[i] == state:
#                             ans += 1
#                             state = 0
#                         else:
#                             state= arr[i]


# ans = work(l1, 0,0)
# print(ans)
