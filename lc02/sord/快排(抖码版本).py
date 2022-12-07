# 快排的抖码版本

from typing import List

nums = [46, 9, 34, 11, 33, 13, 22, 77, 45, 8, 10, 20]


class Solution:
    def patition(self, nums, low, high) -> int:
        if low>= high:
            return
        l = len(nums)
        pivot = nums[high]
        less = low
        # great = low  ,这里其实不用初始化了，下面的great和上面的不同
        if l == 1:
            return 1
        # 这里的逻辑是,great>pivot就只great移动，小于就两个一起移动
        for great in range(low,high):
            if nums[great] < pivot:
                nums[less], nums[great] = nums[great], nums[less]
                less += 1
        nums[less], nums[high] = nums[high], nums[less]
        return less

    def quicksort(self, nums, low, high) -> List[int]:
        # 之前的递归终止条件都没写
        if low >= high:
            return
        mid = self.patition(nums, low, high)
        self.quicksort(nums, low, mid-1)
        self.quicksort(nums, mid + 1, high)
        return nums


if __name__ == '__main__':
    l = len(nums)
    chen = Solution()
    print(chen.quicksort(nums, 0, l - 1))
