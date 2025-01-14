n = int(input())
for i in range(n):
    d,p=map(int,input().split())
    if d != p:
        print("Happy Alex")
        exit()
print("Poor Alex")