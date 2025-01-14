# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==徐嘉期、地球与空间科学学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：

两重条件

先判断是否为4的倍数

再判断能否被400整除

都满足才为闰年



##### 代码

```python
# 
a = int(input () )
if a % 4 == 0:
    if a % 100 == 0 and a % 400 != 0:
        print("N")
    else:
        print("Y")
else:
    print("N")
```



代码运行截图 ==（至少包含有"Accepted"）==

![判断闰年](D:\徐嘉期\北京大学\大一\计算概论\assignment 1\判断闰年.png)

时间：约5min

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：

若为奇数条腿，则直接输出0 0 

若为偶数条腿

​	数目最少时兔子的数目一定为达到上限，mod 4余2或0都可用（+2）//4的方式

​	数目最多时全部为鸡

##### 代码

```python
# 
n = int(input())
if n%2 ==1 :
    print("0 0")
else:
    print((n+2)//4,n//2)
```



代码运行截图 ==（至少包含有"Accepted"）==

![鸡兔同笼](D:\徐嘉期\北京大学\大一\计算概论\assignment 1\鸡兔同笼.png)

时间：约2min

### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：

由黑白染色知，只要格子总数为偶数则一定可以全覆盖，a*b//2即可；为奇数时减一再除以2

##### 代码

```python
# 
str=input().split(' ')
a = int( str[0] )
b= int ( str[1] )
if a*b % 2 ==0:
    print(a*b//2)
else:
    print((a*b-1)//2)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920072911986](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240920072911986.png)

时间：约10min

### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：

n,m除以a向上取整，再乘起来即可

##### 代码

```python
# 
str = input().split(' ')
if int(str[0]) % int(str[2]) == 0:
    n= int(str[0])//int(str[2])
else:
    n= int(str[0])//int(str[2])+1
if int(str[1]) % int(str[2]) == 0:
    m= int(str[1])//int(str[2])
else:
    m= int(str[1])//int(str[2])+1
print(n*m)
```

时间：约20？min

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920073109061](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240920073109061.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：

首先将输入转换为小写

python内置字符串比较即为字典序，直接比较即可

##### 代码

```python
# 
a,b=input(),input()
a=a.lower()
b=b.lower()
if a>b:
    print(1)
elif a<b:
    print(-1)
else:
    print(0)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920073229787](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240920073229787.png)

时间：约10min？

### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：

对每组输入list求和，若大于1即可解决，sum+=1，最后输出sum

##### 代码

```python
# 
total = int(input())
sum_ = 0
for i in range(total):
    curr = sum(map(int,input().split(' ')))
    if curr>1:
        sum_+=1
print(sum_)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920073452152](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20240920073452152.png)

时间：约15？min

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

1）python最基本语法掌握

2）完成题目后看他人代码学会了map,split,sum的用法

3）自己尝试中发现了字符串a>b的比较是按照字典序进行比较，如：ab>aa

4）经过简单思考后，作业比较容易完成，额外练习：补8.23后的每日练习（仍在补作业ing



