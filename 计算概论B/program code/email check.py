def count2(a):
    id=a.index("@")
    sum = 0
    if a[id+1] == '.' or a[id-1]=='.':
        return False
    else:
        for i in range(id+1,len(a)):
            if a[i] == '.':
                return True
        return False

def count1(a):
    sum  = 0
    for i in a:
        if i == '@': sum+=1
    if sum != 1:
        return False

def check(a):
    if count1(a) == False or a[0] == '.' or a[0]=='@' or a[-1]== '.' or a[-1]=='@':
        print("NO")
    else:
        if count2(a) == False:
            print("NO")
        else:
            print("YES")

while(True):
    try:
        a=list(input().strip())
        check(a)        
    except EOFError:
        break