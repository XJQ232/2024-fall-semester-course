# l1=[1,3,5,7,8,10,12]
# l2=[4,6,9,11]
# def checkymd(y,m,d):
#     if m!=2:
#         if m in l1 and d in range(1,32):
#             return True
#         if m in l2 and d in range(1,31):
#             return True
#     else:
#         if checky(y):
#             if d in range(1,30):
#                 return True
#         else:
#             if d in range(1,29):
#                 return True
#     return False
# def checky(y):
#     if y % 4 != 0:
#         return False
#     else:
#         if y % 100 == 0 and y % 400 !=0:
#             return False
#         return True
# y,m,d =(map(int,input().split('-')))
# n = int(input())
# # date[3]+=n
# d+=n
# while True:
#     if checkymd(y,m,d):
#         print('-'.join(tuple(list([str(y),"%02d"%m,"%02d"%d]))))
#         break
#     if m in l1:
#         d-=31
#     elif m in l2:
#         d-=30
#     elif checky(y):
#         d-=29
#     else:
#         d-=28
#     m+=1
#     if m >12:
#         m=1
#         y+=1

import datetime
y,m,d =(map(int,input().split('-')))
n = int(input())
current_date=datetime.datetime(y,m,d)
new_date=current_date+datetime.timedelta(days=n)
print(new_date.strftime("%Y-%m-%d"))
