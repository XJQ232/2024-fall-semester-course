a = float(input())
l1=[0]
curr = 2
while a != 0:
    l1.append(l1[-1]+1/curr)
    curr+=1
    if a<=l1[-1]:
        for i in range(len(l1)-1,0,-1):
            if l1[i-1]<a and a<=l1[i]:
                print(f'{i} card(s)')
                break
        a = float(input())