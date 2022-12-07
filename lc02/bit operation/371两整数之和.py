
from typing import List

a=-12
b=-8


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max [0111 1111 1111 1111 1111 1111 1111 1111]
        MAX = 0x7FFFFFFF
        # mask to get last 32 bits
        # python的int没有范围，他会1111111111111111111111111111111，你要固定四位就是11111111&0000001111
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            # 如果 a > MAX 的话，那么将 a 的补码转成负数的原码  ~(a ^ mask)是将二进制的负数转成十进制的
        return a if a <= MAX else ~(a ^ mask)


if __name__ == '__main__':
    chen = Solution()
    print(chen.getSum(a, b))
