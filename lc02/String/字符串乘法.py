num1 = "123"
num2 = "456"


# 乘法的技巧你要记住，你要是真用我们实际的去算，例如这里你就是会得出三个字符串
# 然后把这三个字符串想加，对应的地方还要补零(因为是斜着的，讨论实际补多少个零很麻烦)

class Solution():
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": return "0"
        m, n = len(num1), len(num2)
        # 999*999也只有99801 六位
        res = [0] * (m + n)
        # 左开右闭合，倒着来的话，-1表示倒着来
        # 从 3 开始分别去乘456 ,所以有两个循环
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                y = int(num2[j])
                sum = res[i + j + 1] + x * y
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10
        index = 1 if res[0] == 0 else 0
        return "".join(str(x) for x in res[index:])


if __name__ == '__main__':
    chen = Solution()
    print(chen.multiply(num1, num2))
