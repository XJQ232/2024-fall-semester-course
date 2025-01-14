n = int(input())
m = int(input())
l1=[]
l2={}
for _ in range(m):
    l1.append(list(map(float,input().split())))
    l2[_]=l1[_][0]*l1[_][1]
    # print(l2[_])
# print(l2)
l3 = sorted(range(m),key= lambda x:l2[x],reverse=True)
# print(l3)
hours = n*2 - 0.5*m
scores = 0
for i in l3:
    # print(i)
    # print(hours)
    # print(scores)
    if not hours:
        break
    if hours >= 5/l1[i][0]:
        hours -= 5/l1[i][0]
        scores += 5*l1[i][1]
    else:
        scores += hours*l1[i][0]*l1[i][1]
        hours = 0
scores=format(scores,'.1f')
print(scores)
exit()

# n = int(input())
# m = int(input())
# tasks = [list(map(float, input().split())) for _ in range(m)]
# values = [task[0] * task[1] for task in tasks]

# # 按照值排序
# sorted_indices = sorted(range(m), key=lambda x: values[x], reverse=True)
# hours = n * 2 - 0.5 * m
# scores = 0

# for i in sorted_indices:
#     if hours <= 0:
#         break
#     time_needed = 5 / tasks[i][0]
#     if hours >= time_needed:
#         hours -= time_needed
#         scores += 5 * tasks[i][1]
#     else:
#         scores += hours * tasks[i][1] / tasks[i][0]
#         hours = 0

# print(format(scores, '.1f'))
