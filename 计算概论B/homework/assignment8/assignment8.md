# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

每次从stack里pop出一个坐标，周长加4，然后减去2*相邻的1数目，状态标记为false，然后将四周状态为True的1的坐标append到stack中

代码：

```python
n,m = map(int,input().split())
check = [[True]*(m+2) for _ in range(n+2)]
matrix = [[0]*(m+2) for _ in range(n+2)]

for _ in range(1,n+1):
    matrix[_][1:-2] = list(map(int,input().split()))
dirct = [(-1,0),(1,0),(0,-1),(0,1)]
stat = False
for i in range(1,n+1):
    if stat:
        break
    for j in range(1,m+1):
        if matrix[i][j] == 1 and check[i][j]:
            stack = {(i,j)}
            stat = True
            break
else:
    print("0")
    exit()
count = 0
while stack:
    count += 4
    x,y = stack.pop()
    check[x][y]= False
    for dx,dy in dirct:
        if matrix[x+dx][y+dy]:
            if not check[x+dx][y+dy]:
                count -= 2
            else:
                stack.add((x+dx,y+dy))
print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241118231941815](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118231941815.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
n = int(input())
matrix = [[] for _ in range(n)]
ans = []
direction = [(0,1),(1,0),(0,-1),(-1,0)]
check = [[True] * n for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int,input().split()))
stack = [(0,0)]
dirc = 0
count = 1
while stack and count <= 4:
    x,y = stack.pop()
    ans.append(matrix[x][y])
    check[x][y] = False
    dx,dy = direction[dirc]
    if x+dx in range(n) and y+dy in range(n) and check[x+dx][y+dy]:
        stack.append((x+dx,y+dy))
        count = 1
    else:
        count += 1
        ans.pop()
        stack.append((x,y))
        dirc = (dirc+1)%4
ans.append(matrix[x][y])
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241118232023060](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118232023060.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d = int(input())
n = int(input())
map1 = []
max1 = 0
l1 = [0]*(1025)
for _ in range(1025):
    map1.append(l1.copy())
for _ in range(n):
    x, y, z = map(int, input().split())
    for i in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            map1[i][j] += z
            if map1[i][j] > max1:
                max1 = map1[i][j]
print(sum([map1[i].count(max1) for i in range(1025)]), max1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241118232044742](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118232044742.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = len(nums)
        dp1 = [1] *len1
        dp2 = [1] * len1
        max1 = 1
        for i in range(1,len1):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp1[i] = max(dp2[j]+1,dp1[i])
                if nums[j] > nums[i]:
                    dp2[i] = max(dp2[i],dp1[j]+1)
            max1 = max(max1,dp1[i],dp2[i])
        return max1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241118232112071](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118232112071.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python
n = int(input())
l1 = list(map(int,input().split()))
dict1 = {}
l2=[]
for i in l1 :
    if i in dict1:
        dict1[i] += i
    else:
        dict1[i] = i
        l2.append(i)
l2.sort()
len1 = len(dict1)
dp1 = [0] * len1
dp2 = [0] * len1
dp1[0] = dict1[l2[0]]
max1 = dp1[0]
for i in range(1,len1):
    dp2[i] = max(dp1[i-1],dp2[i-1])
    if l2[i]-1 == l2[i-1]:
        if i>1:
            dp1[i] = max(dp1[i-2],dp2[i-1]) + dict1[l2[i]]
        if i == 1:
            dp1[i] =dict1[l2[i]]
    else:
        dp1[i] = max(dp2[i-1],dp1[i-1]) + dict1[l2[i]]
    max1 = max(max1,dp1[i],dp2[i])
print(max1)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241118232249404](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118232249404.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

greedy又没想到，只想到了O(n^2^)的暴力算法



代码：

```python
n = int(input())
from bisect import bisect_left
from bisect import bisect_right
while n:
    
    l2 = sorted(list(map(int,input().split())))
    l1 = sorted(list(map(int,input().split())))
    max1 = -float("inf")
    for k in range(n):
        curr = 0
        for i in range(n):
            id1 = (i+k) % n
            if l2[id1] > l1[i]:
                curr += 200
            if l2[id1] < l1[i]:
                curr -= 200
        max1 = max(curr,max1)
    print(max1)
    n = int(input())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241118232937466](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241118232937466.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

AK去年期末考题目，感觉greedy和dp最近做的少了，特别是greedy很难想到



