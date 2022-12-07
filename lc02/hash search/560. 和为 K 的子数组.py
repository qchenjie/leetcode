from typing import List

nums = [1, 1, 1]
k = 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixsum = [0] * (n+1)
        prefixsum[0] = 0
        for i in range(1, n+1):
            prefixsum[i] = prefixsum[i - 1] + nums[i-1]
        res = 0
        # 这里错了弄了一上午
        for i in range(len(prefixsum)):
            diff = prefixsum[i] - k
            for j in range(i):
                if prefixsum[j] == diff:
                    res += 1
        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.subarraySum(nums, k))
