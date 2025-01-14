def check(arr):
    return arr == sorted(arr, reverse=True)


def work(arr, k, id):
    if not k:
        return arr
    if check(arr[id:]) and id:
        return work(arr, k, id-1)
    if check(arr):
        return work(sorted(arr), k-1, len(arr)-1)
    else:
        min1 = len(arr)
        for i in range(id, len(arr)):
            if arr[i] > arr[id] and arr[i] <= min1:
                min1 = arr[i]
                minid = i
        arr[id], arr[minid] = arr[minid], arr[id]
        arr[(id+1):] = sorted(arr[(id+1):])
        return work(arr, k-1, len(arr)-1)


n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr_out = work(arr, k, n-1)
print(*arr_out)
