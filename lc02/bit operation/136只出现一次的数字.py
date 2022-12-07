a = [4, 1, 2, 1, 2]

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for num in nums:
            single ^= num
        return single


if __name__ == '__main__':
    chen = Solution()
    print(chen.singleNumber(a))
