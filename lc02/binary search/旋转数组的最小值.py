# 二分查找
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        # 这里的细节就是 要left < right 而不是等于
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # 第二个细节就是right = mid 而不是mid+1
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    # 这玩意必须要有序
    a = [0, 1, 2]
    chen = Solution()
    print(chen.findMin(a))
