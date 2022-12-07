
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n != 0:
            # 下面的用完之后都是有右移的,所以当前位就是最后一位
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.myPow(3, 15))
