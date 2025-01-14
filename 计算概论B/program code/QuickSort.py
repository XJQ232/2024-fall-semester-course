def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return Quicksort(left) + [pivot] + Quicksort(right)


arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20,
          17, 10]
print(arr_in)
arr_out = Quicksort(arr_in)
print(arr_out)
