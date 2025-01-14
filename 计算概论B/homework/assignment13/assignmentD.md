# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：



代码：

```python
number = int(input())
l1={chr(x+ord('A')):x for x in range(12)}
for _ in range(number):
    check = [False] * 12
    weight = [0]*12
    for i in range(3):
        str1 = list(input().split())
        if str1[2] == 'even':
            for i in str1[0]:
                check[l1[i]]=True
                weight[l1[i]]=0
            for i in str1[1]:
                check[l1[i]]=True
                weight[l1[i]]=0
        if str1[2] == 'up':
            count = 0
            for i in str1[0]:
                if weight[l1[i]] == -1:check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]] and weight[l1[i]] != -1:weight[l1[i]]=1
                
            for i in str1[1]:
                if weight[l1[i]] ==1 :check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=-1
            if count == 7:
                for i in l1:
                    if not (i in str1[1] or i in str1[0]) :
                        check[l1[i]] = True
        else:
            count = 0
            for i in str1[1]:
                if weight[l1[i]] == -1:check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=1
            for i in str1[0]:
                if weight[l1[i]] ==1 :check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=-1
            if count == 7:
                for i in l1:
                    if not (i in str1[1] or i in str1[0]):
                        check[l1[i]] = True
    for i in range(12):
        if weight[i]>0 and not check[i]:
            ans = chr(i+ord('A'))
            print(f'{ans} is the counterfeit coin and it is heavy.')
        if weight[i]<0 and not check[i]:
            ans = chr(i+ord('A'))
            print(f'{ans} is the counterfeit coin and it is light.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224231825077](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224231825077.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：



代码：

```python
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# n,m = map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0]*m for _ in range(n)]
# max1 = 0
# check = [[True] * m for _ in range(n)]
# def dfs(x,y):
#     if dp[x][y] > 0 :
#         return dp[x][y]
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0<= nx < n and 0<= ny < m:
#             if matrix[x][y] > matrix[nx][ny]:
#                 dp[x][y] = max(dp[x][y],dfs(nx,ny))
#     dp[x][y] += 1
#     return dp[x][y]
# for i in range(n):
#     for j in range(m):
#         max1= max(max1,dfs(i,j))
# print(max1)
from functools import lru_cache

dx = [1,-1,0,0]
dy = [0,0,-1,1]
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
max1 = 0
check = [[True] * m for _ in range(n)]
@lru_cache(maxsize=2048)
def work(x,y):
    
    temp1 = 0
    check1 = True
    for k in range(4):
        nx = x+dx[k]
        ny = y + dy[k]
        if 0<=  nx < n and 0<= ny < m:
            if matrix[x][y] > matrix[nx][ny]:
                if not check[nx][ny]:
                    temp1 = max(temp1,dp[nx][ny])
                else:
                    temp1 = max(work(nx,ny),temp1)
                check1 = False
    if check1:
        dp[x][y] = 1
        check[x][y] = False
        return 1
    return temp1+1

for i in range(n):
    for j in range(m):
        if check[i][j]:
            dp[i][j] = work(i,j)
            max1 = max(max1, dp[i][j])
print(max1)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241224232300578](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224232300578.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：



代码：

```python
n = int(input())
matrix=[[1]*(n+2) for _ in range(n+2)]
check=[[True]*(n+2) for _ in range(n+2)]
dirc = [(-1,0),(1,0),(0,-1),(0,1)]
l1={'x':(0,1),'y':(1,0)}
start=[]
for i in range(1,n+1):
    matrix[i][1:n] = list(map(int,input().split()))
    for j in range(1,n+1):
        if matrix[i][j] == 9:
            endx=i
            endy=j
        if matrix[i][j] == 5:
            start.append((i,j))
# print(start,endx,endy)
# print(matrix)
if start[0][0]==start[1][0]:
    stat = 'x'
else:
    stat = 'y'
pos=[start[0]]
while pos:
    x,y=pos.pop()
    # print(pos)
    # print(x,y)
    # print(matrix)
    # print(check)
    
    if x==endx and y == endy:
        print("yes")
        break
    if x+l1[stat][0] == endx and y+l1[stat][1] == endy:
        print("yes")
        break
    check[x][y] = False
    for i,j in dirc:
        if check[x+i][y+j]:
            if matrix[x+i][y+j] != 1 and matrix[x+i+l1[stat][0]][y+j+l1[stat][1]] != 1:
                pos.append((x+i,y+j))
else:
    print("no")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224232318739](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224232318739.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：



代码：

```python
m = int(input())
n = int(input())
l1 = list((input().split()))
for i in range(n):
    for j in range(i+1,n):
        if l1[j]+l1[i] > l1[i] + l1[j]:
            l1[i],l1[j] = l1[j],l1[i]
dp = ['0']*(m+1)
for i in range(n):
    for j in range(m,len(l1[i])-1,-1):
        
        dp[j] = str(max(int(dp[j]),int(dp[j-len(l1[i])]+l1[i])))
        # print(dp)
print(int(dp[-1]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224232336426](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224232336426.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：



代码：

```python
from itertools import product
from copy import deepcopy
l1 = list(product([0,1],repeat=6))
matrix=[list(map(int,input().split())) for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for l2 in l1:
    temp1=deepcopy(matrix)
    l3=[list(l2)]
    for i in range(6):
        if l3[0][i]:
            temp1[0][i]=1^temp1[0][i]
            for k in range(4):
                nx = 0 + dx[k]
                ny = i + dy[k]
                if 0<=nx<5 and 0<= ny < 6:
                    temp1[nx][ny] = 1^temp1[nx][ny]
    for i in range(1,5):
        l3.append([])
        for j in range(6):
            # print(l3)
            if temp1[i-1][j]:
                l3[i].append(1)
                temp1[i][j]=1^temp1[i][j]
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<5 and 0<= ny < 6:
                        temp1[nx][ny] = 1^temp1[nx][ny]
            else:
                l3[i].append(0)
    if sum(temp1[-1]) == 0:
        for i in range(5):
            print(*l3[i])
        exit()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224232523964](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224232523964.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：



代码：

```python
l,n,m = map(int,input().split())
d=[0]
for _ in range(n):
    d.append(int(input()))
d.append(l)
d.sort()
left = 1
right=l
ans = 0
while left <= right:
    mid = (left+right)//2
    count = 0
    j = 0
    for i in range(1,n+2):
        if d[i]-d[j] < mid:
            count += 1
        else:
            j = i
    if count > m:
        right = mid - 1
    else:
        ans,left =mid, mid + 1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224232543596](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241224232543596.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

作业做了两天。。。还是看了答案才能想到思路的。。。正在为机考祈福中

正在复习之前的知识，还没有放弃

