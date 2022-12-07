def demo01():
    chen = input()
    print(chen)


def demo02():
    n = int(input().strip())
    print(n)


def demo03():
    n = list(map(int, input().split()))
    print(n)


# 输入一个矩阵
def demo04():
    d = [list(map(int, input().split()))]
    print(d)


# 对比input().split()和 不用split()的区别
def demo05():
    n = list(input().split())
    print(n)


if __name__ == "__main__":
    demo05()
