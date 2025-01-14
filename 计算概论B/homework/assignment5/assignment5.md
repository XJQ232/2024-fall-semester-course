# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
curr = 0
while True:
    p,e,i,d = map(int,input().split())
    curr += 1
    if p==-1:exit()
    while (p-e)%28 != 0:
        p+=23
    while (p-i)%33 != 0:
        p+=644
    if p <= d:
        p = p+21252 - d
    else:
        p -= d
    print(f'Case {curr}: the next triple peak occurs in {p} days.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028134315949](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134315949.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：



代码：

```python
money = int(input())
l1=list(map(int,input().split()))
l1.sort()
total = 0
i = 0
j = -1
check = [True]*len(l1)
for i in range(len(l1)):
    if money >= l1[i]:
            money -= l1[i]
            total += 1
    else:
        
        for j in range(-1,-len(l1),-1):
            if i == j:
                if money > l1[i]:
                    total +1
                break
            if l1[j] + money >= l1[i] and check[j] and total > 0:
                money = money+l1[j] - l1[i]
                check[j] = False
                break
print(total)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241028134516677](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134516677.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n = int(input())
l1 = list(map(int, input().split()))
if n == 1:
    print('1')
    print('0.00')

else:
    l2 = sorted(range(1, n+1), key=lambda x: l1[x-1])
    l1.sort()
    sum1 = 0
    for i in range(n):
        sum1 += (n-i-1)*l1[i]
    average = format(sum1/n, '.2f')
    print(*l2)
    print(average)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028134540455](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134540455.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：



代码：

```python
month = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac',
         'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
day = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen',
       'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
n = int(input())
print(n)
for _ in range(n):
    str1 = list(input().split(' '))
    str1[0] = str1[0].strip('.')
    days = int(str1[0])
    days += 20 * month.index(str1[1]) + 365*int(str1[2]) + 1
    years = (days-1) // 260
    days = days % 260
    print(days % 13 if days % 13 else '13', day[days % 20-1], years)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028134554584](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134554584.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python
n = int(input())
lx = []
lh = []
for _ in range(n):
    x,h = map(int,input().split())
    lx.append(x)
    lh.append(h)
if n == 1:
    print(1)
else:
    curr = lx[0]
    total = 1
    for i in range(1,n-1):
        if lx[i] - lh[i] > curr:
            curr = lx[i]
            total += 1
            continue
        if lx[i] + lh[i] < lx[i+1]:
            curr = lx[i] + lh[i]
            total += 1
            continue
        else:
            curr = lx[i]
    total += 1
    print(total)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028134657921](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134657921.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：



代码：

```python
from math import sqrt
n,d = map(int,input().split())
curr = 1
while n:
    check = True
    l1=[]
    l2=[]
    for _ in range(n):
        x,y=map(int,input().split())
        if y > d:
            check = False
        else:
            l1.append(x-sqrt(-pow(y,2)+pow(d,2)))
            l2.append(x+sqrt(-pow(y,2)+pow(d,2)))
    if check == False:
        print(f"Case {curr}: -1")
    else:
        l2_sorted = sorted(l2)
        l1_sorted = [x for x,_ in sorted(zip(l1,l2),key=lambda pair:pair[1])]
        total = 1
        ed = l2_sorted[0]
        if n > 1:
            for i in range(1,n):
                if l1_sorted[i] > ed:
                    total += 1
                    ed = l2_sorted[i]
        print(f"Case {curr}: {total}")
    curr += 1
    input()
    n,d = map(int,input().split())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241028134735647](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241028134735647.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最近每日选做做得有点少了，感觉是期中逼近和题目难度上来导致，每道题都要想好一会（悲）

不过感觉学习算法、学习母题还是比较重要的，这次地雷达安装，如果课上没有听区间问题的五种类型，自己独立地做出来可能要花费比较久的时间，没有否定独立思考的重要性，但感觉自己目前学的代码知识还是比较少（？）很多时候比较难想到正确的解法

（还有个感觉是自己的脑袋目前有点像单线程的，打10大排序代码的时候遇到分治和递归的时候容易转不过弯，需要python tutor来可视化代码，自己想还是太难想到了





