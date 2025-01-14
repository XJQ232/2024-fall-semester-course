# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：



代码

```python
# 
n,m=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort()
sum=0
for i in range(m):
    if l1[i]<0:
        sum+=l1[i]
print(-sum)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241017175717474](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017175717474.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：



代码

```python

n = int(input())
l1=list(map(int,input().split()))
l1.sort(reverse=True)
curr=j=0
while 2*curr<= sum(l1):
    curr+=l1[j]
    j+=1
print(j)

```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241017175754464](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017175754464.png)

### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：



代码

```python

n = int(input())
for i in range(n):
    m = int(input())
    row = list(map(int,input().split()))
    line = list(map(int,input().split()))
    row.sort();line.sort()
    min1=row[0]*m+sum(line)
    min2=line[0]*m+sum(row)
    print(min(min1,min2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241017175813355](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017175813355.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：



代码

```python

n = int(input())
l1=sorted(list(map(int,input().split())))
dic1={}
check = [False] * 5
set1 = set(l1)
for i in set1:
    dic1[i]=l1.count(i)
    check[i]=True
total = 0;spare = 0
if check[4]:
    total += dic1[4]
if check[3]:
    total += dic1[3]
    spare += dic1[3]
if check[2]:
    total += (dic1[2]-1)//2 + 1
    spare += 2*(dic1[2] % 2)
if check[1]:
    if spare < dic1[1]:
        total += (dic1[1]-spare-1)//4+1
print(total)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241017175913707](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017175913707.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：



代码

```python

from math import isqrt
def seive_of_Euler(limit):
    isprime=[0]*(limit+1)
    isprime[0]=isprime[1]=1
    prime=[]
    for i in range(limit+1):
        if isprime[i] == 0:
            prime.append(i)
        for j in prime:
            if i*j >limit:
                break
            isprime[i*j]=1
            if i%j == 0:break
    return prime
n = int(input())
l1 = list(map(int,input().split()))
m=isqrt(max(l1))+1
prime=seive_of_Euler(m)
ans=set(p*p for p in prime)
for i in l1:
    if i in ans:
        print("YES")
    else:
        print("NO")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241017175924398](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017175924398.png)



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：



代码

```python

n = int(input())
l1 = list(input().split())
len1 = len(l1)
l2=[]
for i in range(10):
    l2.append([])
for i in l1:
    l2[int(i[0])].append(i)
for i in range(1,10):
    len2 = len(l2[i])
    for j in range(len2-1):
        for k in range(j+1,len2):
            num1 = int(l2[i][j]+l2[i][k])
            num2 = int(l2[i][k]+l2[i][j])
            if num1 <= num2:
                c = l2[i][j]
                l2[i][j] = l2[i][k]
                l2[i][k] = c
max1=''
min1=''
for i in range(9,0,-1):
    for j in l2[i]:
        max1 = max1+j
    l2[i].reverse()
for i in range(1,10):
    for j in l2[i]:
        min1 = min1 + j
print(max1,min1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241017181357490](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241017181357490.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最近感觉各科任务量比较大，虽然往计概上投入的时间仍然很多，但相比之前可能还是会有所下降，而且明显感到题目难度变大，有些题目不是那么容易做出来了，但是还是会认真思考的

感觉自己可能还是要赶紧调整一下方法：1，做完题还是要看答案，不能因为时间紧张而选择为了完成题目而做题，感觉这样提升较慢，不如把一道题学透，宁可学精；2，除了打代码实践，理论的学习也要抓起来了，得自己去努力看算法书，最近的题目让自己感觉到自己思维可能还是比较的局限；3，多和同学交流，自己面对着ants题目迟迟没有进展，但和朋友最近一次聊天后才意识到这道脑筋急转弯该怎么做

悲，起飞但又没完全起飞

