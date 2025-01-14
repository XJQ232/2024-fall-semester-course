n = int(input())
curr = 1
temp = 1
for _ in range(1,n):
    temp,curr = curr,curr+temp
print(curr)