# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：



代码：

```python
l1 = list(map(int,input().split()))
max1 = 0
len1 = len(l1)
l2 = []
for i in range(1,len1):
    l2.append(l1[i]-l1[i-1])
dp = [0]*len1
dp[0] = l2[0]
for i in range(1,len1):
    dp[i] = max(dp[i],dp[i-1]+l2[i-1])
    max1 = max(max1,dp[i])
print(max1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209223954689](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241209223954689.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：



代码：

```python
def  work(sum1,arr,num):
    temp = sum1 / num
    if arr[0] > temp:
        return work(sum1-arr[0],arr[1:],num-1)
    return temp
n,k = map(int,input().split())
l1 = sorted(list(map(int,input().split())),reverse=True)
s1 = sum(l1)
ans = format(work(s1,l1,k),'.3f')
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241209224019262](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241209224019262.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：



代码：

```python
l1 = list(map(int,input().split(',')))
dp1 = l1.copy()
dp2 = [-float('inf')]+[0]*(len(l1)-1)
max1 = l1[0]
for i in range(1,len(l1)):
    dp1[i] = max(dp1[i],dp1[i-1]+l1[i])
    dp2[i] = max(dp2[i-1]+l1[i],dp1[i-1])
    max1 = max(max1,dp1[i],dp2[i])
# print(dp1,dp2)
print(max1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209224108117](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241209224108117.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：



代码：

```python
from collections import defaultdict
n, m = map(int, input().split())
price =[input().split() for _ in range(n)]
coupon = [input().split() for _ in range(m)]
temp = [0]*m
min1 = float("inf")

def dfs(id,sum1):
    global min1
    if id == n:
        cou = 0
        for i in range(m):
            curr = 0
            for s in coupon[i]:
                x,y = map(int,s.split('-'))
                if temp[i] >= x:
                    curr = max(curr,y)
            cou += curr
        min1 = min(min1,sum1 - sum1//300*50 - cou)
        return
    for s in price[id]:
        x,y = map(int,s.split(':'))
        temp[x-1] += y
        dfs(id+1,sum1+y)
        temp[x-1] -= y
dfs(0, 0)
print(min1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209225518556](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241209225518556.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：



代码：

```python
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
from collections import deque
matrix = []
for i in range(n):
    matrix.append(list(input()))
stack1 = deque()

def dfs(x,y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] == '1':
                matrix[nx][ny] = '2'
                stack1.append((nx,ny,0))
                dfs(nx,ny)
    return

def solve():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                matrix[i][j] = '2'
                stack1.append((i,j,0))
                dfs(i,j)
                return

solve()

while stack1:
    x,y,step = stack1.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx and nx < n and 0<= ny and ny < n:
            if matrix[nx][ny] == '1':
                print(step)
                exit()
            if matrix[nx][ny] == '0':
                stack1.append((nx,ny,step+1))
                matrix[nx][ny] = '2'
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210000252574](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241210000252574.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：



代码：

```python
n = int(input())
a,b = map(int,input().split())
l1 = []
for _ in range(n):
    x,y = map(int,input().split())
    l1.append((x*y,x,y))
l1.sort()
# print(l1)
sum1 = a
for i in range(n-1):
    sum1 *= l1[i][1]
sum1 = sum1//(l1[-1][-1])
print(sum1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209224039212](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241209224039212.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

孤岛距离卡了好几天，一直TLE也不知道为什么，看了答案对比发现这次问题出在了visited这个辅助集合上，虽然add操作和判断是否in的操作都是O（1）的时间复杂度，但这道题直接原地修改比建立辅助集合确实快了很多



