n = int (input())
for i in range(n):
    m,l=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l3=sorted(range(m),key=lambda x:l1[x])
    l4=sorted(l2)
    l5=[0]*m
    for i in range(m):
        l5[l3[i]]=l4[i]
    print(' '.join(list(map(str,l5))))

# n = int (input())
# for i in range(n):
#     m,n=map(int,input().split())
#     l1=list(map(int,input().split()))
#     l2=list(map(int,input().split()))
#     l3=[]
#     for j in l1:
#         l3.clear()
#         for k in l2:
#             if abs(j-k) <= n:
#                 l3.append(k)
#         best=min(l3)
#         print(best,end=' ')
#         l2.remove(best)
#     print()