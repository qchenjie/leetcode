# 二分查找
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 如果数组本身就有小数，那就置为n+1
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            # 把当前位置的正数变成负数
            if (num <= n):
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    chen = Solution()
    print(chen.firstMissingPositive(nums))
