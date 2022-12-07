# 这个题目真牛逼
# 比较不偷第一个,看剩余的最大值,和不偷最后一个剩余的最大值
# [2,7,9,3,1] = max([7,9,3,1]，[2,7,9,3])

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob(nums: List[int]) -> int:
            n = len(nums)
            if n==1:
                return nums[0]
            dp = [0]* (n+1)
            dp[1] = nums[0]
            for i in range (2,n+1):
                dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
            return max(dp)

        n = len(nums)
        if n == 1: return nums[0]
        not_rob_first_house = rob(nums[1: n])
        not_rob_last_house = rob(nums[0: n -1])
        return max(not_rob_first_house, not_rob_last_house)



if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    # nums = [1, 2, 3, 1]
    print(solution.rob(nums))
