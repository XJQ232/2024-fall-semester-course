# total = int(input())
# sum= 0
# for i in range(total):
#     curr = 0
#     str = input().split(' ')
#     for j in str:
#         curr += int(j)
#     if curr >= 2:
#         sum+=1
# print(sum)

total = int(input())
sum_ = 0
for i in range(total):
    curr = sum(map(int,input().split(' ')))
    if curr>1:
        sum_+=1
print(sum_)

# n = int(input())
# cnt = 0
# for i in range(n):
#     s = sum(map(int, input().split()))
#     if s > 1: cnt += 1
# print(cnt)