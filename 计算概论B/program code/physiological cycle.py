curr = 0
while True:
    p,e,i,d = map(int,input().split())
    curr += 1
    if p==-1:exit()
    while (p-e)%28 != 0:
        p+=23
    while (p-i)%33 != 0:
        p+=644
    if p <= d:
        p = p+21252 - d
    else:
        p -= d
    print(f'Case {curr}: the next triple peak occurs in {p} days.')