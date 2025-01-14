# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：



代码：

```python
Test = int(input())
dx = [0,0 ,1 ,1,1,-1,-1,-1]
dy = [1,-1,-1,0,1,-1, 0, 1]

def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] == 'W':
        return True
    return False

for _ in range(Test):
    n,m = map(int,input().split())
    matrix = [[] for _ in range(n)]
    max1 = 0
    stack = [(0,0)]
    
    for i in range(n):
        matrix[i] = list(input())
        for j in range(m):
            if matrix[i][j] == 'W':
                stack.pop()
                stack.append((i,j))
    # print(stack)
    while True:
        # print(stack,)
        curr = 0
        while stack:
            x,y = stack.pop()
            if matrix[x][y] == 'W':
                curr += 1
                matrix[x][y] = '.'
                for i in range(8):
                    nx,ny = x+dx[i],y+dy[i]
                    if check(matrix,nx,ny):
                        stack.append((nx,ny))
        max1 = max(max1,curr)
        # print(matrix,max)
        stat = False
        for i in range(n):
            if stat:break
            for j in range(m):
                if matrix[i][j] == 'W':
                    stack.append((i,j))
                    stat = True
                    break
        if not stack:break
    print(max1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241125124621685](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124621685.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：



代码：

```python
from collections import deque

n,m = map(int,input().split())
matrix = [[] for i in  range(n)]
visited = set()
dx=[0,0,1,-1]
dy=[-1,1,0,0]
def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] != 2 and (x,y) not in visited:return True
    else:return False
for _ in range(n):
    matrix[_] = list(map(int,input().split()))
stack = deque([(0,0)])
step = -1
stat = True
while stack and stat:
    step += 1
    curr = stack.copy()
    # print(step)
    # print(curr)
    # print()
    while curr and stat:
        
        x,y = curr.pop()
        stack.popleft()
        visited.add((x,y))
        # print(x,y)
        # print(stack)
        # print(curr)
        if matrix[x][y] == 1:
            print(step)
            stat = False
            break
        for i in range(4):
            if check(matrix,x+dx[i],y+dy[i]):
                stack.append((x+dx[i],y+dy[i]))
        # print(x,y)
        # print(stack)
        # print(curr)
        # print()
if stat:print("NO")
    
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241125124653091](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124653091.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
from collections import deque
import sys
sys.setrecursionlimit(1<<30)
count = 0
def check(mat,x,y):
    if x in range(n) and y in range(m) and mat[x][y] == 0:
        return True
    return False

def dfs(mat, x, y):
    global count
    if len(inqueue) == total:
        count += 1
        return
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        # print(nx,ny,count)
        if check(mat,nx,ny):
            mat[nx][ny] = 1
            inqueue.add((nx,ny))
            dfs(mat, nx, ny)
            mat[nx][ny] = 0
            inqueue.remove((nx,ny))

Test = int(input())

for _ in range(Test):
    count = 0
    n, m, x, y = map(int, input().split())
    dx = [1, 1, -1, -1, 2, -2, 2, -2]
    dy = [2, -2, 2, -2, 1, 1, -1, -1]
    matrix = [[0]*m for _ in range(n)]
    matrix[x][y] = 1
    total = n*m
    inqueue = set()
    inqueue.add((x,y))
    dfs(matrix, x, y)
    print(count)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241125124717524](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124717524.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：



代码：

```python
n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
visited = [[True]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans=[]

def check(mat, x, y):
    if x in range(n) and y in range(m) and mat[x][y]:
        return True
    return False


def dfs(mat, x, y, value,step):
    global max1
    global ans
    if x == n-1 and y == m-1:
        if value > max1:
            max1 = value
            ans = step.copy()
            # print(ans)
        return
    visited[x][y] = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if check(visited, nx, ny):
            step.append((nx,ny))
            dfs(mat, nx, ny, value+mat[nx][ny],step)
            step.pop()
    visited[x][y] = True


max1 = -float("inf")
for i in range(n):
    matrix[i] = list(map(int, input().split()))
visited[0][0] = False
dfs(matrix, 0, 0, matrix[0][0],[(0,0)])
for i in ans:
    x,y = i
    print(x+1,y+1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241125124841556](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124841556.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：

数学问题

代码：

```python
from math import comb
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return(comb(m+n-2,m-2))
        
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241125124921751](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124921751.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：



代码：

```python
from math import isqrt
def check(a):
    if a == 0:return False
    return isqrt(a)**2 == a
def dfs(s,step):
    global stat
    num = int(s)
    if stat:return
    if step == len(n)-1:
        if check (num):
            stat =True
        return
    else:
        if check(num):
            dfs(n[step+1],step+1)
        dfs(s+n[step+1],step+1)
        
n = input()
stat = False
dfs(n[0],0)
print("Yes" if stat else "No")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241125124943659](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241125124943659.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

目前感觉良好，至少模板题都能打出来，还在跟进每日选做中



