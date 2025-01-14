def heapify(arr, n, i):
    largest = i
    lson = 2*i + 1
    rson = 2*i + 2
    if lson < n and arr[largest] <= arr[lson]:
        largest = lson
    if rson < n and arr[largest] <= arr[rson]:
        largest = rson
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,n,i)
    # for i in range(n):
    #     arr[0],arr[-i-1] = arr[-i-1],arr[0]
    #     heapify(arr,n-i-1,0)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    return arr

arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20,
          17, 10]
print(arr_in)
arr_out = heapsort(arr_in)
print(arr_out)
