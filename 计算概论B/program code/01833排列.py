m = int(input())


def check(arr):
    return arr == sorted(arr,reverse=True)


def work(arr, k, id):
    if not k:
        return arr
    # if id > 0 and arr[id] > arr[id - 1]:
    #     if not check(arr[id:]):
    #         arr[id], arr[id-1] = arr[id-1], arr[id]
    #         arr[id:] = sorted(arr[id:])
    #     else:
    #         minid = arr.index(min(arr[id:]))
    #         arr[id-1], arr[minid] = arr[minid], arr[id-1]
    #         arr[id:] = sorted(arr[id:])
    #         return work(arr, k-1, len(arr)-1)
    #     print(arr)
    #     return work(arr, k-1, len(arr)-1)
    # if id > 0 and arr[id] < arr[id-1]:
    #     print(arr)
    #     return work(arr, k, id-1)
    # if not id:
    #     print(arr)
    #     return work(sorted(arr), k-1, len(arr)-1)
    if check(arr[id:]) and id:
        return work(arr,k,id-1)
    if check(arr):
        return work(sorted(arr),k-1,len(arr)-1)
    else:
        min1 = len(arr)
        for i in range(id,len(arr)):
            if arr[i] > arr[id] and arr[i] <= min1:
                min1 = arr[i]
                minid = i
        arr[id],arr[minid]=arr[minid],arr[id]
        arr[(id+1):]=sorted(arr[(id+1):])
        return work(arr,k-1,len(arr)-1)

for _ in range(m):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_out = work(arr, k, n-1)
    print(*arr_out)
