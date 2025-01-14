from math import ceil
n = int(input())
if n < 6 : exit()
for _ in range(6,n+1):
    curr = _**3
    for i in range(2,n):
        i1=i**3
        if i1>curr:
            break
        for j in range(i,n):
            j1=j**3
            if i1+j1 > curr:
                break
            for k in range(j,n):
                k1=k**3
                if i1+j1+k1 > curr:
                    break
                if i1+j1+k1 == curr:
                    print(f"Cube = {_}, Triple = ({i},{j},{k})")