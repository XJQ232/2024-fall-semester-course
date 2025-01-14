# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：按照题目意思打代码，注意az之间的转换



代码

```python
n = int(input())%26
str1 = input()
for i in str1:
    if ord(i) in range(65,91):
        if (ord(i)-n-64)%26+64 != 64:
            print(chr((ord(i)-n-64)%26+64),end='')
        else:
            print('Z',end='')
    if ord(i) in range(97,123):
        if (ord(i)-n-96)%26+96 != 96:
            print(chr((ord(i)-n-96)%26+96),end='')
        else:
            print('z',end='')

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011234042815](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234042815.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：

两个list，只看前两位即可

代码

```python
str1 = list(input().split())
num1 = int(str1[0][0])*10+int(str1[0][1])
num2 = int(str1[1][0])*10+int(str1[1][1])
print(num1 + num2)	

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011234100405](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234100405.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：按照题目意思打代码即可



代码

```python
n = int( input())
l1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
l2=['1','0','X','9','8','7','6','5','4','3','2']
for _ in range(n):
    str1 = input()
    sum_ = 0
    for i in range(17):
        sum_ += int(str1[i])*l1[i]
    sum_ %= 11
    if l2[sum_] == str1[17]:
        print("YES")
    else:
        print("NO")
    

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011234119931](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234119931.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：按照题目意思打代码即可



代码

```python
n = int(input())
while n!= 1:
    if n%2 == 1:
        print(f"{n}*3+1={n*3+1}")
        n=n*3+1
    else:
        print(f"{n}/2={n//2}")
        n//=2
print("End")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011234139494](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234139494.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：第一反应是贪心+暴力，但对字典、tuple的熟练度还不够高，代码比较冗长



##### 代码

```python
# 
l1 = ['I','V',"X","C","M","L",'D']
str1 = input()
if str1[0] in l1:
    len1 = len(str1)
    total = 0
    for i in range(len1):
        if i < len1 - 1:
            if str1[i] == 'I' and (str1[i+1] == 'X' or str1[i+1] == 'V'):total -= 1;continue
            if str1[i] == 'X' and (str1[i+1] == 'L' or str1[i+1] == 'C'):total -= 10;continue
            if str1[i] == 'C' and (str1[i+1] == 'D' or str1[i+1] == 'M'):total -= 100;continue
            else:
                if str1[i] == 'I':total += 1
                if str1[i] == 'V':total += 5
                if str1[i] == "X":total += 10
                if str1[i] == 'L':total += 50
                if str1[i] == 'C':total += 100
                if str1[i] == 'D':total += 500
                if str1[i] == 'M':total += 1000
        else:
            if str1[i] == 'I':total += 1
            if str1[i] == 'V':total += 5
            if str1[i] == "X":total += 10
            if str1[i] == 'L':total += 50
            if str1[i] == 'C':total += 100
            if str1[i] == 'D':total += 500
            if str1[i] == 'M':total += 1000
    print(total)
else:
    n = int(str1)
    while n - 1000 >= 0:
        print('M',end = '')
        n-=1000
    if n - 900 >= 0:
        print('CM',end='')
        n-=900
    if n - 500 >= 0:
        print('D',end='')
        n -= 500
    if n - 400 >= 0:
        print('CD',end='')
        n-=400
    while n -100 >= 0:
        print("C",end='')
        n-=100
    if n -90 >= 0:
        print("XC",end='')
        n-=90
    if n-50 >= 0:
        print("L",end='')
        n-=50
    if n-40 >= 0:
        print("XL",end='')
        n-=40
    while n-10 >=0:
        print("X",end='')
        n-=10
    if n-9>=0:
        print("IX",end='')
        n-=9
    if n-5>=0:
        print("V",end='')
        n-=5
    if n-4>=0:
        print("IV",end='')
        n-=4
    while(n-1>=0):
        print("I",end='')
        n-=1
    print()
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011234230977](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234230977.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：

贪心：有点难描述，但突然想到用两组max和min

代码

```python
n,d=map(int,input().split())
l0=[]
l1=[]
l2=[]
l3=[]
max1 = 0
min1 = 999999999
max2 = 0
min2 = 999999999
for _ in range(n):
    l0.append(int(input()))
l2=l0.copy()
k = len(l2)
while k > 0:
    l1.clear()
    l3.clear()
    max1=l2[0]
    min1=l2[0]
    max2=l2[0]
    min2=l2[0]
    check = True
    for i in range(k):
        if not(abs(min1-l2[i])>d or abs(l2[i] - max1) > d):
            if check:
                l1.append(l2[i])
                l3.append(i)
                if min1 >= l2[i]:
                    min1 = l2[i]
                if max1 <= l2[i]:  
                    max1 = l2[i]
            else:
                if not(abs(min2-l2[i])>d or abs(l2[i] - max2) > d):
                    l1.append(l2[i])
                    l3.append(i)
        else:
            check = False
            if min2 >= l2[i]: min2 = l2[i]
            if max2 <= l2[i]: max2 = l2[i]

    l1.sort()
    for i in l1:
        print(i)
    for i in sorted(l3,reverse=True):
        l2.pop(i)
    k = len(l2)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011234255873](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241011234255873.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

罗马数字转换这道题目让自己认识到了对字典和tuple的熟练度太低，没有想到简单的对应关系，同时也告诫自己如果第一反应是暴力模拟，要考虑是否实现难度过大，不要过于相信自己的if-else逻辑水平

排队这道题有点意思，如果当时是在考场上的话可能会因为罗马数字耗时太多而没时间做，自己对这个贪心算法也想了一段时间，特别是独自想到用两组max和min的时候基本就解决问题了，唯一的遗憾是之前没怎么用pop，还是问了一次GPT，不算是完全独立完成

总结就是语法基本掌握，但有些板块熟练度还有待提高，不能等到用的时候才发现其实是一知半解









