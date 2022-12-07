def partition(arr, low, high):
    pivot = arr[low]

    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [92, 96, 100, 110, 42, 35, 30, 88, 88]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in arr:
    print(i)
