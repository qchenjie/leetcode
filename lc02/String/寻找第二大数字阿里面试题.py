from typing import List

nums = [5, 7, 1, 2, 3, 4, 78, -90, 565, 4454546, 0]


class Solution:
    def getSecondMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        for i in nums:
            if i > first:
                second = first
                first = i
            elif i > second:
                second = i
        return second


if __name__ == '__main__':
    chen = Solution()
    print(chen.getSecondMax(nums))
