import math
while True:
    sum = 0
    l1= list(map(int,input().split()))
    sum = sum+ l1[5]+l1[4]
    if l1[0]-11*l1[4]>=0:
        l1[0]=l1[0]-11*l1[4]
    else:
        l1[0]=0
    sum += l1[3]
    if l1[1]-5*l1[3]>=0:
        l1[1]=l1[1]-5*l1[3]
    else:
        if l1[0]-20*l1[3]+4*l1[1]>0:l1[0]=l1[0]-20*l1[3]+4*l1[1];l1[1]=0
        else:l1[0]=l1[1]=0
    sum += l1[2]//4
    l1[2]=l1[2]%4
    if l1[2]==0:
        sum+=math.ceil(l1[1]/9)
        l1[1]%=9
        if l1[1]!=0:
            if l1[0]-36+4*l1[1]>=0:
                l1[0]=l1[0]-36+4*l1[1]
            else:
                l1[0]=0
        sum+=math.ceil(l1[0]/36)
    if l1[2]==1:
        sum+=1
        if l1[1]>=5:
            l1[1]-=5
            if l1[0]>=7:
                l1[0]-=7
            else:
                l1[0]=0
        else:
            if l1[0]-27+4*l1[0]>=0:
                l1[0]=l1[0]-27+4*l1[0]
                l1[1]=0
            else:
                l1[0]=l1[1]=0
        sum+=l1[1]//9
        l1[1]%=9
        if l1[1]!=0:
            if l1[0]-36+4*l1[1]>=0:
                l1[0]=l1[0]-36+4*l1[1]
            else:
                l1[0]=0
        sum+=math.ceil(l1[0]/36)
    if l1[2]==2:
        sum+=1
        if l1[1]>=3:
            l1[1]-=3
            if l1[0]>=6:
                l1[0]-=6
            else:
                l1[0]=0
        else:
            if l1[0]-18+4*l1[1]>=0:
                l1[0]=l1[0]-18+4*l1[1]
                l1[1]=0
            else:
                l1[0]=0
                l1[1]=0
        sum+=l1[1]//9
        l1[1]%=9
        if l1[1]!=0:
            if l1[0]-36+4*l1[1]>=0:
                l1[0]=l1[0]-36+4*l1[1]
            else:
                l1[0]=0
        sum+=math.ceil(l1[0]/36)
    if l1[2]==3:
        sum+=1
        if l1[1]>=1:
            l1[1]-=1
            if l1[0]>=5:
                l1[0]-=5
            else:
                l1[0]=0
        else:
            if l1[0]>=9:
                l1[0]-=9
            else:
                l1[0]=0
        sum+=l1[1]//9
        l1[1]%=9
        if l1[1]!=0:
            if l1[0]-36+4*l1[1]>=0:
                l1[0]=l1[0]-36+4*l1[1]
            else:
                l1[0]=0
        sum+=math.ceil(l1[0]/36)
    if sum>0:
        print(sum)
    else:
        exit(0)

# import sys
# sys.setrecursionlimit(30000)
# min = 99999
# def work(total,a,b,c,d,e,f):
#     global min
#     if a**2 + b**2 + c**2 + d**2 + e**2 == 0:
#         if total < min:
#             min = total
#         return
#     if f>=9:
#         if a>0:
#             work(total,a-1,b,c,d,e,f-1)
#         if b>0:
#             work(total,a,b-1,c,d,e,f-4)
#         if c>0:
#             work(total,a,b,c-1,d,e,f-9)
#         else:
#             return
#     elif f>=4:
#         if a>0: 
#             work(total,a-1,b,c,d,e,f-1)
#         if b>0:
#             work(total,a,b-1,c,d,e,f-4)
#         else:
#             return
#     elif f>0:
#         if a>0:
#             work(total,a-1,b,c,d,e,f-1)
#         else:
#             return
#     if e>0:
#         work(total+1,a,b,c,d,e-1,f+11)
#     if d>0:
#         work(total+1,a,b,c,d-1,e,f+20)
#     if d==0 and e==0 and c>0:
#         work(total+1,a,b,c-1,d,e,f+27)
# while True:
#     l1=list(map(int,input().split()))
#     if sum(l1) == 0:
#         break
#     total = 0
#     min = 99999
#     work (total+l1[5],l1[0],l1[1],l1[2],l1[3],l1[4],0)
#     print(min)

# min_value = 99999

# def work(total, a, b, c, d, e, f):
#     global min_value
#     if a**2 + b**2 + c**2 + d**2 + e**2 == 0:
#         if total < min_value:
#             min_value = total
#         return

#     if f >= 9:
#         work(total, a - 1, b, c, d, e, f - 1)
#         work(total, a, b - 1, c, d, e, f - 4)
#         work(total, a, b, c - 1, d, e, f - 9)
#     elif f >= 4:
#         work(total, a - 1, b, c, d, e, f - 1)
#         work(total, a, b - 4, c, d, e, f - 4)
#     elif f > 0:
#         work(total, a - 1, b, c, d, e, f - 1)

#     if e > 0:
#         work(total + 1, a, b, c, d, e - 1, f + 11)
#     if d > 0:
#         work(total + 1, a, b, c, d - 1, e, f + 20)
#     if d == 0 and e == 0 and c > 0:
#         work(total + 1, a, b, c - 1, d, e, f + 27)

# while True:
#     l1 = list(map(int, input().split()))
#     if sum(l1) == 0:
#         break
#     total = l1[5]  # Initialize total directly with l1[5]
#     min_value = 99999  # Reset the min_value for each input
#     work(total, l1[0], l1[1], l1[2], l1[3], l1[4], 0)
#     print(min_value)