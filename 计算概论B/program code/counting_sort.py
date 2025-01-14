def counting_sort(arr):
    max_value = max(arr)
    count=[0]*(max_value+1)
    for i in arr:
        count[i] += 1
    ans=[]
    for i in range(max_value+1):
        ans.extend([i]*count[i])
    return ans

arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20,
17, 10]
print(arr_in)
arr_out = counting_sort(arr_in)
print(arr_out)

# def CountingSort(arr):
#     max_value = max(arr)
#     count = [0] * (max_value + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for i in range(max_value + 1):
#         sorted_arr.extend([i] * count[i])
#     return sorted_arr
# if __name__ == "__main__":
#     arr_in = [6, 5, 18, 2, 16, 15, 19, 13, 10, 12, 7, 9, 4, 4, 8, 1, 11, 14, 3, 20,
#     17, 10]
#     print(arr_in)
#     arr_out = CountingSort(arr_in)
#     print(arr_out)