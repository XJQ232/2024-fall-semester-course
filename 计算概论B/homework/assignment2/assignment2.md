# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：

曼哈顿距离

##### 代码

```python
# 
a=['']*5
for i in range(5):
    a[i]=input().split()
    for j in a[i]:
        if j == '1':
            print(abs(i-2)+abs(a[i].index(j)-2))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924112843543](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924112843543.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：

找到b离a最近的倍数

##### 代码

```python
# 
n = int(input())
a=['']*2
for i in range(n):
    a=list(map(int,input().split()))
    if a[0] % a[1] == 0:
        print('0')
    else:
        print(a[1]*(a[0]//a[1]+1) - a[0])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924113049067](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924113049067.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：

状态储存器：目前警力，初始为0，每次加上当前输入数值

​			一旦变为负数，清零并且启动计数器

计数器：表明未被处理的案件，初始为零，当输入为负数时计数器加一，当输入为正数时暂停计数器并启动状态储存器

最后输出计数器

##### 代码

```python
# 
n = int(input())
curr = 0
total = 0
m=list(map(int,input().split()))
for i in range(n):
    if curr > 0:
        curr += m[i]
    else:
        if m[i]>0:
            curr = m[i]
        else:
            total +=1
print(total)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924113202183](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924113202183.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

bool数组，初始为1，在特定区域内的变为0，最后对数组求和

##### 代码

```python
# 
L,M=map(int,input().split())
b=[1]*(L+1)
for i in range(M):
    m,n=map(int,input().split())
    for i in range(m,n+1):
        b[i]=0
sum=0
for i in range(L+1):
    sum+=b[i]
print(sum)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924113633113](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924113633113.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：

获取各个数位并计算

##### 代码

```python
# 
def check(a):
    hund=a//100
    ten=a//10 %10
    one=a%10
    if hund**3+ten**3+one**3 == a:
        return True
m,n = map(int,input().split())
num=0
for i in range(m,n+1):
    if check(i):
        num+=1
        if num !=1:
            print(' ',end='')
            print(i,end='')
        else:
            print(i,end='')
if num == 0:
    print("NO")
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924113817646](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924113817646.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：

对于每个学生：

若出发时间为负数，则不用考虑

若出发时间为正数，则计算到达时间

最后取到达时间最早即可

##### 代码

```python
# 
from math import ceil
n = int(input())
while n!=0:
    min = 999999999
    for i in range(n):
        v,t=map(int,input().split())
        if t>=0 and ceil(16200/v+t)<min:
            min = ceil(16200/v+t)
    print(min)
    n = int(input())
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924132938974](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240924132938974.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

1）ride to school有意思，数学模型想明白后发现题目不难

2）完成每日选做，开始自己找题目做



