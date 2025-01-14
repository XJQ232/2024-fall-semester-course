import math
while True:
    space1 = 0
    space2 = 0
    sum = 0
    l1= list(map(int,input().split()))
    sum = sum+ l1[5]+l1[4]+l1[3]
    space1 += l1[4]*11
    space2 += l1[3]*5
    sum += math.ceil(l1[2]/4)
    l1[2]=l1[2]%4
    if l1[2]==1:
        space2 += 5
        space1 += 7
    if l1[2]==2:
        space2 += 3
        space1 += 6
    if l1[2]==3:
        space2 += 1
        space1 += 5
    if l1[1] - space2 >=0:
        l1[1] -= space2
        sum += math.ceil(l1[1]/9)
        l1[1] %= 9
        if l1[1]>0:
            space1 += 36 - 4*l1[1]
    else:
        space1 += 4*(space2-l1[1])
    if l1[0] - space1 >0:
        l1[0]-=space1
        sum += math.ceil(l1[0]/36)
    if sum>0:
        print(sum)
    else:
        exit(0)
 