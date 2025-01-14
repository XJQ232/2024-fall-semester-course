n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
dp1 = l1.copy()
max1 = l1[0]
max2 = l2[0]
dp2 = l2.copy()
max_ = max(max1,max2)
for i in range(1,n):
    dp2[i] = max(dp2[i], max1+l2[i])
    dp1[i] = max(dp1[i], max2+l1[i])
    max1 = max(max1, dp1[i])
    max2 = max(max2, dp2[i])
    max_ = max(max1, max2)
print(max_)

# # 手动输入
# N = int(input())

# # 初始化数组，注意要确保数组大小为 N + 1
# h = [[0] * 3 for _ in range(N + 1)]
# f = [[0] * 3 for _ in range(N + 1)]

# # 读取h数组，第二行和第三行分别为h[i][1]和h[i][2]
# h_values_1 = list(map(int, input().split()))
# h_values_2 = list(map(int, input().split()))

# # 确保输入的长度正确
# if len(h_values_1) != N or len(h_values_2) != N:
#     print("输入的长度与N不匹配，请重新输入。")
# else:
#     # 填充h数组
#     for i in range(1, N + 1):
#         h[i][1] = h_values_1[i - 1]
#         h[i][2] = h_values_2[i - 1]

#     # 初始化f数组
#     f[1][0] = 0
#     f[1][1] = h[1][1]
#     f[1][2] = h[1][2]

#     # 动态规划计算
#     for i in range(2, N + 1):
#         f[i][0] = max(f[i - 1][0], max(f[i - 1][1], f[i - 1][2]))
#         f[i][1] = max(f[i - 1][0], f[i - 1][2]) + h[i][1]
#         f[i][2] = max(f[i - 1][0], f[i - 1][1]) + h[i][2]

#     # 输出结果
#     print(max(f[N][0], max(f[N][1], f[N][2])))
