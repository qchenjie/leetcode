# 爬楼梯

def loft(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return loft(n - 1) + loft(n - 2) + loft(n - 3)


print(loft(1000))
