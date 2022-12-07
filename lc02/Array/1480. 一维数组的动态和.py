from typing import List

nums = [1, 2, 3, 4]


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        left_total=0
        for i in range(len(nums)):
            nums[i]+=left_total
            left_total=nums[i]
        return nums


if __name__ == '__main__':
    chen = Solution()
    print(chen.runningSum(nums))
