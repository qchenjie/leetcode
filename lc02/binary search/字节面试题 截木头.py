# 二分查找
from typing import List

# 我们的目的 ，是找到k个m长度的
# 这里是我格局小了，非得用数组存着？
class Solution:
    def cutWood(self, nums: List[int], k) -> int:
        # 先找到最大值
        maxValue = max(nums)
        left, right = 1, maxValue
        while left < right:
            mid = left + (right - left) // 2
            if self.calWoodCnt(nums, mid) < k:
                right = mid-1
            else:
                left = mid +1
        return left

    # 计算arrs数组中，能截取多少个nums
    def calWoodCnt(self, arrs, nums):
        cnt = 0
        for i in arrs:
            cnt += i//nums
        return cnt


if __name__ == '__main__':
    nums = [4, 7, 2, 10, 5]
    target = 5
    chen = Solution()
    print(chen.cutWood(nums,target))
