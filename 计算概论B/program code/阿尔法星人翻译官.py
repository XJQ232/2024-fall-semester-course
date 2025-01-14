dict1= {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, "seven":7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
dict2={ 'hundred':100, "thousand":1000, "million":1000000}
l1 = list(input().split())
check = 1
k = 0
if l1[0] == 'negative':
    check = -1
    k = 1
temp = 0
curr = 0
ans = []
for i in range(k,len(l1)):
    if l1[i] in dict1:
        temp += dict1[l1[i]]
    else:
        if not curr:
            curr = dict2[l1[i]]
            temp *= dict2[l1[i]]
            ans.append(temp)
        else:
            if dict2[l1[i]] < curr:
                temp *= dict2[l1[i]]
                curr = dict2[l1[i]]
                ans.append(temp)
            else:
                curr = dict2[l1[i]]
                temp += ans.pop()
                temp *= curr
                ans.append(temp)
        temp = 0
ans.append(temp)
temp = ans[0]
# print(ans)
if len(ans) > 1:
    for i in range(1,len(ans)):
        if temp < ans[i]:
            temp = int(str(temp) + str(ans[i]))
        else:
            temp += ans[i]
print(temp*check)