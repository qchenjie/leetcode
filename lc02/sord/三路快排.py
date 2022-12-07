from typing import List
import random

nums = [46, 9, 34, 11, 33, 20, 22, 20, 45, 8, 10, 20]


class Solution():
    # 这里的核心思想是: 当前小于pivot就和less交换，大于pivot就和graet交换，否则就
    def sortArray(self, nums, lo, hi):
        if lo >= hi:
            return
        i = random.randint(lo, hi)
        nums[i], nums[hi] = nums[hi], nums[i]
        pivot, less, great = nums[hi], lo, hi
        i = lo
        while i <= great:
            if nums[i] < pivot:
                # 当前小于pivot就和less交换
                nums[i], nums[less] = nums[less], nums[i]
                less, i = less + 1, i + 1
            elif nums[i] > pivot:
                # 大于pivot就和graet交换
                nums[i], nums[great] = nums[great], nums[i]
                great -= 1
            else:
                i += 1
        return less, great

    def quick_sort(self, nums, lo, hi) -> List[int]:
        if lo >= hi:
            return
        less, great = self.sortArray(nums, lo, hi)
        self.quick_sort(nums, lo, less - 1)
        self.quick_sort(nums, great + 1, hi)
        return nums


if __name__ == '__main__':
    l = len(nums)
    chen = Solution()
    print(chen.quick_sort(nums, 0, l-1))
