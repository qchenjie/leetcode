a=27
b=4
from typing import List


class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if a == INT_MIN and b == -1:
            return INT_MAX

        sign = -1 if (a > 0) ^ (b > 0) else 1

        a, b = abs(a), abs(b)
        ans = 0
        for i in range(31, -1, -1):
            if (a >> i) - b >= 0:
                a = a - (b << i)
                ans += 1 << i
        # bug 修复：因为不能使用乘号，所以将乘号换成三目运算符
        return ans if sign == 1 else -ans


if __name__ == '__main__':
    chen = Solution()
    print(chen.divide(a, b))
