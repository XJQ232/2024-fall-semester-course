n,w = map(int,input().split())
stack =[]
for _ in range(n):
    value,weight = map(int,input().split())
    stack.append((value/weight,weight,value))
stack.sort(reverse=True)
total = 0
value = 0
i = 0
while total < w:
    if i >= n:break
    if total + stack[i][1]<=w:
        value += stack[i][2]
        total += stack[i][1]
    else:
        value += stack[i][0]*(w-total)
        total = w
    i+= 1
value=format(value,'.1f')
print(value)