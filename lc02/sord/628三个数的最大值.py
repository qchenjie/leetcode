from typing import List

nums = [5, 7, 1, 2, 3, 4]


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = [float('inf')] * 2
        max1, max2, max3 = [float('-inf')] * 3
        for num in nums:
            min1, min2, _ = sorted([min1, min2, num])
            _, max3, max2, max1 = sorted([max1, max2, max3, num])
        return max(max1 * max2 * max3, max1 * min1 * min2)

    def maximumProduct01(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])


if __name__ == '__main__':
    chen = Solution()
    print(chen.maximumProduct01(nums))
