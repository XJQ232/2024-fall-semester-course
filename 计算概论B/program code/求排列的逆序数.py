def mergesort(arr,count):
    len1 = len(arr)
    if len1 <= 1:
        return arr,count
    else:
        mid = len1//2
        left,count1 = mergesort(arr[:mid],0)
        right,count2 = mergesort(arr[mid:],0)
        i,j=0,0
        arr2=[]
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr2.append(left[i])
                i+=1
            else:
                arr2.append(right[j])
                count += len(left) - i
                j += 1
        arr2 = arr2 + left[i:]+right[j:]
        count = count + count1 + count2
        return arr2,count 

n = int(input())
l1 = list(map(int,input().split()))
l1_out, ans = mergesort(l1,0)
print(ans)