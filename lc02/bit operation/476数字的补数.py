from typing import List

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while (num & mask) > 0:
            mask <<= 1
        return ~mask ^ num


if __name__ == '__main__':
    chen = Solution()
    print(chen.findComplement(5))
