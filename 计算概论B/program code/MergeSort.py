def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return Merge(left, right)


def Merge(left, right):
    ans =[]
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j+= 1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20,
17, 10]
print(*arr_in)
arr_out=MergeSort(arr_in)
print(*arr_out)