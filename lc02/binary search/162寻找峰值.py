# 二分查找
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [5, 6, 5, 7, 4, 1, 2, 1, 3]
    target = 7
    chen = Solution()
    print(chen.findPeakElement(nums))
