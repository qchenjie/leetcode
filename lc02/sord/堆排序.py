def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # 如果大于左边的
    if l < n and arr[largest] < arr[l]:
        largest = l
    # 如果大于右边的
    if r < n and arr[largest] < arr[r]:
        largest = r
    # 如果不等于i(原来是等于i的，说明有交换)，上面的交换只是标识做了交换，下面就是真正的交换了
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
    # 这里最难懂了，是因为你只是维护了当前三个元素的最大值，它更新之后，他下面还有值要更新
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # 这就是一个次数，你想想上面右节点是下面的公式
    # right = 2*i + 2
    # 那最后一个节点的是不是n-2//2 这里不减2了，直接除以二就好了，越界就越界咯
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    # 经过上面的建堆之后，就变成一个大根堆，也就是13 11 12 5 6 7 （层序也就是数组的顺序）
        # 一个个交换元素，不断的把子节点元素和顶点做交换
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 11, 7, 5, 6, 13]
heapSort(arr)
n = len(arr)
print("排序后")
print(arr)
