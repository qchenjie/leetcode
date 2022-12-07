nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 如果K很大之类的
        k = k % n
        start = count = 0
        while count < n:
            current = start
            prev = nums[start]
            # 下面是一次循环，不断的去交换
            while True:
                next = (current + k) % n  # 被替代变量的位置
                nums[next], prev = prev, nums[next]  # 不断的和prev做交换
                current = next
                count += 1
                if start == current:
                    break
            start += 1


if __name__ == '__main__':
    chen = Solution()
    print(chen.rotate(nums,k))
