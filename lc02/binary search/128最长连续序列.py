# 二分查找
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        lookup_table = set(nums)
        max_cnt = 1
        for num in nums:
            # 这里会存在重复计算，为什么会产生以及如何解决，请参考 issue：
            # https://gitee.com/douma_edu/douma_algo_training_camp/issues/I4H4RZ
            if num - 1 in lookup_table:
                continue
            curr_num = num
            cur_count = 1
            while curr_num + 1 in lookup_table:
                # 这个while就那种看如果有连续的
                curr_num += 1
                cur_count += 1
            max_cnt = max(max_cnt, cur_count)
        return max_cnt


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    chen = Solution()
    print(chen.longestConsecutive(nums))
