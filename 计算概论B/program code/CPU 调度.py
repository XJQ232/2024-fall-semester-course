n = int(input())
total = 0
curr = []
min1 = 999999
for _ in range(n):
    x,y =map(int,input().split())
    y+= 1
    curr.append((y,x))
curr.sort(reverse=True)
read = [curr[i][1] for i in range(n)]
write = [curr[i][0] for i in range(n)]
time1 = 0
time2= 0
for i in range(n):
    
    time1 = time1 + read[i]
    if i<n-1:
        time2 = max(write[i]+time1,read[i+1]+time1,time2)
    else:
        time2 = max(write[i]+time1,time2)
    # print(read[i],write[i],time1,time2)
print(time2-1)