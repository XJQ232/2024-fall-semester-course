s1 = input().lower().strip()
l1 = ' '+input().lower()+' '
count = 0
id1= float('inf')
for i in range(1,len(l1)-len(s1)+1):
    if l1[i:i+len(s1)] == s1 and l1[i-1]==' ' and l1[i+len(s1)]==' ': 
        count += 1
        id1 = min(id1,i-1)
if count:
    print(count ,id1)
else:
    print('-1')