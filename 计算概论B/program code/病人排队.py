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
        