number = int(input())
l1={chr(x+ord('A')):x for x in range(12)}
for _ in range(number):
    check = [False] * 12
    weight = [0]*12
    for i in range(3):
        str1 = list(input().split())
        if str1[2] == 'even':
            for i in str1[0]:
                check[l1[i]]=True
                weight[l1[i]]=0
            for i in str1[1]:
                check[l1[i]]=True
                weight[l1[i]]=0
        if str1[2] == 'up':
            count = 0
            for i in str1[0]:
                if weight[l1[i]] == -1:check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]] and weight[l1[i]] != -1:weight[l1[i]]=1
                
            for i in str1[1]:
                if weight[l1[i]] ==1 :check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=-1
            if count == 7:
                for i in l1:
                    if not (i in str1[1] or i in str1[0]) :
                        check[l1[i]] = True
        else:
            count = 0
            for i in str1[1]:
                if weight[l1[i]] == -1:check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=1
            for i in str1[0]:
                if weight[l1[i]] ==1 :check[l1[i]]=True;weight[l1[i]]=0
                if check[l1[i]]:count += 1
                if not check[l1[i]]:weight[l1[i]]=-1
            if count == 7:
                for i in l1:
                    if not (i in str1[1] or i in str1[0]):
                        check[l1[i]] = True
    for i in range(12):
        if weight[i]>0 and not check[i]:
            ans = chr(i+ord('A'))
            print(f'{ans} is the counterfeit coin and it is heavy.')
        if weight[i]<0 and not check[i]:
            ans = chr(i+ord('A'))
            print(f'{ans} is the counterfeit coin and it is light.')
