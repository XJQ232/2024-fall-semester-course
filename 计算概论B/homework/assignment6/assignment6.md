# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：



代码：

```python
l1=['A','B','C']
def work(n,a,b,c):
    str1 = l1[a]+'->'+l1[b]+'\n'
    if n==1:
        return str1
    return work(n-1,a,c,b) + str1 + work(n-1,c,b,a)
n = int(input())
a = 1 << n
print(a-1)
ans = work (n,0,2,1)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101232854518](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101232854518.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：



代码：

```python
def work(n,l2,l3,ans):
    if n == 1:
        ans.append(l3+l2)
        return
    for i in range(n):
        l3.append(l2[i])
        work (n-1,l2[0:i]+l2[i+1:],l3,ans)
        l3.pop()
    return ans
s = int(input())
if s == 1:print("1")
else:
    l1=[]
    for i in range(1,s+1):
        l1.append(str(i))
    output = work(s,l1,[],[])
    for i in output:
        print(*i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241101232919385](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101232919385.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：



代码：

```python
n = int(input())
l1 = list(map(int,input().split()))
dp=[1]*n
max1=1
for i in range(1,n):
    for j in range(i):
        if l1[j] >= l1[i]:
            dp[i] = max(dp[i],dp[j]+1)
    if dp[i] > max1:
        max1 = dp[i]
print(max1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101233001253](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101233001253.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
n,weight_max = map(int,input().split())
value = list(map(int,input().split()))
weight = list(map(int,input().split()))
dp_value = [0]*(weight_max+1)
max1 = 0
for i in range(n):
    if weight[i] <= weight_max:
        for j in reversed(range(weight_max+1-weight[i])):
            dp_value[weight[i]+j]=max(dp_value[weight[i]+j],dp_value[j]+value[i])
            max1 = max(max1,dp_value[weight[i]+j])
print(max1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101233025640](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101233025640.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：



代码：

```python
def eight_queen(l1,id,ans):
    if id==8:
        ans.append(l1.copy())
        return
    len1 = len(l1)
    for i in range(8):
        valid = True
        for j in range(len1):
            if i == l1[j]  or abs(id - j) == abs(l1[j] - i):
                valid = False
                break
        if valid:
            l1.append(i)
            eight_queen(l1,id+1,ans)
            l1.pop()
    return

ans=[]
eight_queen([],0,ans)
ans_=[[x+1 for x in i] for i in ans]
n = int(input())
for _ in range(n):
    print(*ans_[int(input())-1],sep='')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101233047361](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101233047361.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python
length,a,b,c = map(int,input().split())
l1=[a,b,c]
dp_max = [0]*(length+1)
for i in range(length+1):
    for j in l1:
        if i > j:
            if dp_max[i-j]:
                dp_max[i]=max(dp_max[i],dp_max[i-j]+1)
        if i==j:
            dp_max[i]=max(dp_max[i],1)
print(dp_max[length])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101233124290](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241101233124290.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

看了一点算法图解后感觉提升嘎嘎明显，感觉这次作业手感变好了，还要继续看算法书



