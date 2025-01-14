n = int(input())
arr=[0]*n
for i in range(n):
    arr[i]=int(input())
y=m=d=0
for i in range(n):
    y=arr[i]//10000
    m=(arr[i]//100)%100
    d=arr[i]%100
    if m <3:
        m+=12
        y-=1
    w=(y%100+y%100//4+(y//100)//4-2*(y//100)+(26*(m+1))//10+d-1)%7
    if w==1:
        print("Monday")
    elif w==2:
        print("Tuesday")
    elif w==3:
        print("Wednesday")
    elif w==4:
        print("Thursday")
    elif w==5:
        print("Friday")
    elif w==6:
        print("Saturday")
    else:
        print("Sunday")