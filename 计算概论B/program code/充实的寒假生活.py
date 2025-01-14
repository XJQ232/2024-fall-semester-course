n = int(input())
start = []
end = []
for _ in range(n):
    x,y = map(int,input().split())
    if y <= 60:
        start.append(x)
        end.append(y)
start_sorted = [x for x,_ in sorted(zip(start,end),key=lambda pair:pair[1])]
end_sorted = sorted(end)
len1 = len(start)
total = 1
curr = end_sorted[0]
for i in range(1,len1):
    if start_sorted[i] > curr:total+=1;curr = end_sorted[i]
print(total)