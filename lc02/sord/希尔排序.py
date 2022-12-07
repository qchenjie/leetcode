def shell_sort(alist):
    step = len(alist) // 2
    while step > 0:
        for i in range(step, len(alist)):
            # 在索引为step到len（L）上，比较L[i]和L[i-step]的大小
            while i >= step and alist[i] < alist[i - step]:
                # 这里可以调整step从小到大或者从大到小排列
                alist[i], alist[i - step] = alist[i - step], alist[i]
                i -= step
        step //= 2


# 下面给的示例也很好，不要轻易的更改了

if __name__ == "__main__":
    # li = [1, 3, 2, 32, 5, 4]
    li = [9, 1, 5, 8, 3, 7, 4, 6, 2]
    print(li)
    shell_sort(li)
    print(li)
