def merge(arr, l, m, r):
    # 合并的时候要新开数组，大小要合并的数组相加
    # 下面是   左右两边要合并的大小，    你定下心看，不难的
    n1 = m - l + 1  # 0到4有五个数字
    n2 = r - m

    # 创建临时数组(合并的时候要新开数组，大小为 要合并的数组相加)
    L = [0] * (n1)
    R = [0] * (n2)

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]  # 本来是L[i] = arr[L]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    #  开始合并，这两个数组是在各自的地方都是有序的，直接用两个指针指着两个数组的第一个要比较的地方

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
    # 像二叉树一样，一直递进去，先递归左边的，再递归右边的
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [8, 4, 5, 7, 1, 3, 6, 2]
n = len(arr)
print("给定的数组")
for i in range(n):
    print("%d" % arr[i]),

mergeSort(arr, 0, n - 1)
print("\n\n排序后的数组")

print(arr)