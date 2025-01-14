# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>徐嘉期、地空</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n = int(input())
id_old=[]
age_old=[]
id_young=[]
for _ in range(n):
    temp = list(input().split())
    id1 = temp[0]
    age = int(temp[1])
    if age >= 60:
        check = True
        for i in range(len(age_old)):
            if age_old[i] < age:
                age_old = age_old[:i]+[age]+age_old[i:]
                id_old = id_old[:i]+[id1]+id_old[i:]
                check = False
                break
        if check:
            age_old.append(age)
            id_old.append(id1)
        # print(age_old)
        # print(id_old)
    else:
        id_young.append(id1)
ans = id_old+id_young
for i in ans:
    print(i)
        
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108000817940](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108000817940.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,m1,m2 = map(int,input().split())
matrix1 = [[0]*n for _ in range(n)]
matrix2 = [[0]*n for _ in range(n)]
matrix3 = [[0]*n for _ in range(n)]
for _ in range(m1):
    x,y,v = map(int,input().split())
    matrix1[x][y]=v
for _ in range(m2):
    x,y,v = map(int,input().split())
    matrix2[x][y]=v
ans = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            matrix3[i][j] += matrix1[i][k]*matrix2[k][j]
        if matrix3[i][j]:
            l1 = [str(i),str(j),str(matrix3[i][j])]
            ans.append(' '.join(l1))
for i in ans:
    print(i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241108000827800](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108000827800.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
cases = int(input())
for _ in range(cases):
    n,m,b = map(int,input().split())
    dict1 = {}
    time = []
    for __ in range(n):
        t,x = map(int,input().split())
        if t in dict1:
            dict1[t].append(x)
        else:
            dict1[t] = [x]
            time.append(t)
    # print(dict1)
    # print(time)
    time.sort()
    check = False
    for i in time:
        if check:
            break
        dict1[i].sort(reverse=True)
        length = min(m,len(dict1[i]))
        for j in range(length):
            b -= dict1[i][j]
            if b <= 0:
                print(i)
                check = True
                break
    if not check:
        print("alive")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108000851332](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108000851332.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：



代码：

```python
n ,amount =map(int,input().split())
dp = [float("inf")]*(amount+1)
check = [False]*(amount+1)
l1 = list(map(int,input().split()))
for i in l1 :
    if i <= amount:
        dp[i] = 1
for i in range(1,amount+1):
    temp = dp[i]
    for j in l1:
        if i > j:
            temp = min(temp,dp[i-j]+1)
    if temp != dp[i]:
        dp[i] = temp
        check[i] =True
print(dp[amount] if check[amount] else "-1")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108000918012](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108000918012.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：



代码：

```python
dict1= {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, "seven":7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
dict2={ 'hundred':100, "thousand":1000, "million":1000000}
l1 = list(input().split())
check = 1
k = 0
if l1[0] == 'negative':
    check = -1
    k = 1
temp = 0
curr = 0
ans = []
for i in range(k,len(l1)):
    if l1[i] in dict1:
        temp += dict1[l1[i]]
    else:
        if not curr:
            curr = dict2[l1[i]]
            temp *= dict2[l1[i]]
            ans.append(temp)
        else:
            if dict2[l1[i]] < curr:
                temp *= dict2[l1[i]]
                curr = dict2[l1[i]]
                ans.append(temp)
            else:
                curr = dict2[l1[i]]
                temp += ans.pop()
                temp *= curr
                ans.append(temp)
        temp = 0
ans.append(temp)
temp = ans[0]
# print(ans)
if len(ans) > 1:
    for i in range(1,len(ans)):
        if temp < ans[i]:
            temp = int(str(temp) + str(ans[i]))
        else:
            temp += ans[i]
print(temp*check)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108000932649](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108000932649.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：



代码：

```python
n = int(input())
start = []
end = []
for _ in range(n):
    x,y = map(int,input().split())
    if y <= 60:
        start.append(x)
        end.append(y)
start_sorted = [x for x,_ in sorted(zip(start,end),key=lambda pair:pair[1])]
end_sorted = sorted(end)
len1 = len(start)
total = 1
curr = end_sorted[0]
for i in range(1,len1):
    if start_sorted[i] > curr:total+=1;curr = end_sorted[i]
print(total)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108001019769](C:\Users\徐嘉期\AppData\Roaming\Typora\typora-user-images\image-20241108001019769.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

除了排队和翻译，其他感觉都是上课或者作业的模板题（？）基本不太需要花时间，默写代码即可

但是如果期末考考第一题可能会心态爆炸（悲）被自己之前不怎么在意的排序稳定性绊倒了

倒数第二题感觉是自己的运气题，考试时不确定自己能否想出这样的模拟方案（悲）

还是做题太少了



