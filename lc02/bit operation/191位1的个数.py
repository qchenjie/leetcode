
from typing import List

nums= 15

class Solution:
    def hammingWeight(self, n:int) -> int:
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.hammingWeight(nums))
