n = int(input())

for _ in range(n):
    s=[]
    set1=set()
    for i in range(3):
        s.append(list(input().split()))
    for i in range(3):
        for j in range(2):
            for k in s[i][j]:
                set1.add(k)
    stat1 = True
    # print(set1)
    for i in range(2):
        for j in range(65,77):
            c = chr(j)
            if c not in set1:
                continue
            stat = True
            for k in range(3):
                if c in s[k][0]:
                    if i == 0:
                        if s[k][2] != 'down':
                            stat = False
                    if i == 1:
                        if s[k][2] != 'up':
                            stat = False
                if c in s[k][1]:
                    if i == 1:
                        if s[k][2] != 'down':
                            stat = False
                    if i == 0:
                        if s[k][2] != 'up':
                            stat = False
                if c not in s[k][0] and c not in s[k][1]:
                    if s[k][2]!='even':stat = False
            if stat:
                if i == 0:
                    print(f"{c} is the counterfeit coin and it is light.")
                if i == 1:
                    print(f"{c} is the counterfeit coin and it is heavy.")