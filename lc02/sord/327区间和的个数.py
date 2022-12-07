nums = [-2, 5, -1]
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 就是上面的列出的i=0,1,2
        lenth_arr = len(nums)
        ans = 0  # 返回个数
        for i in range(lenth_arr):
            for j in range(i + 1, lenth_arr + 1):
                temp = nums[i:j]
                if lower <= sum(temp) <= upper:
                    ans += 1
        return ans





if __name__ == '__main__':
    chen = Solution()
    print(chen.countRangeSum(nums, -2, 2))
