from math import sqrt
def check(a):
    for i in range(3,int(sqrt(a)+1),2):
        if a%i == 0:
            return False
    return True
n = int(input())
# print(check(n))
total = 0
if n==1 or n==0:
    print("1")
    exit(0)
if n % 2 ==0:
    if n%4 == 0:
        print("0")
        exit(0)
    else:
        n/=2
        total+=1
i=3
while i<=n:
    if check(i):
        if n%i == 0:
            if n% i**2!=0:
                n/=i
                total+=1
            else:
                print("0")
                exit(0)
    i+=2
if total== 0:total=1
if total % 2 ==0:
    print("1")
else:
    print("-1")

# from math import sqrt

# def mu(n):
#     # Step 1: 判断n是否存在平方质因数
#     def has_square_factor(n):
#         for i in range(2, int(sqrt(n)) + 1):
#             if n % (i * i) == 0:
#                 return True
#         return False

#     # Step 2: 计算n的质因数个数
#     def count_prime_factors(n):
#         count = 0
#         if n % 2 == 0:
#             count += 1
#             while n % 2 == 0:
#                 n //= 2
#         for i in range(3, int(sqrt(n)) + 1, 2):
#             if n % i == 0:
#                 count += 1
#                 while n % i == 0:
#                     n //= i
#         if n > 2:
#             count += 1
#         return count

#     # 根据规则判断μ(n)的值
#     if n == 1:
#         return 1
#     if has_square_factor(n):
#         return 0
#     else:
#         prime_factor_count = count_prime_factors(n)
#         if prime_factor_count % 2 == 0:
#             return 1
#         else:
#             return -1

# # 输入正整数n
# n = int(input())
# print(f"{mu(n)}")

