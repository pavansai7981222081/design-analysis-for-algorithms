def min_max(arr, start, end):
   
    if start == end:
        return arr[start], arr[start]


    if end == start + 1:
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]

 
    mid = (start + end) // 2
    min1, max1 = min_max(arr, start, mid)
    min2, max2 = min_max(arr, mid + 1, end)

    return min(min1, min2), max(max1, max2)

arr = [3, 5, 1, 9, 7, 2, 8, 4]
min_val, max_val = min_max(arr, 0, len(arr) - 1)
print("Minimum value:", min_val)
print("Maximum value:", max_val)


