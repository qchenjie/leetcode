s = "aabaabasdgsgsfgsgsgsgsgsgsgsgsgwgtyiukdthdjfseteethdrhsrhdtjfjjjkhjkhjkhklhklhklh"
from typing import List

class Solution():
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            str = self.rotate(list(s), i)
            str=''.join(str)
            if s == str:
                return True
        return False

    # 这里就是供下面调用的
    def reverse(self, nums, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            # temp = nums[start]
            # nums[start] = nums[end]
            # nums[end] = temp
            start, end = start + 1, end - 1

    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        # 防止K过大
        k = k % n
        # 第一步先整体反转
        self.reverse(nums, 0, n - 1)
        # 第二步是反转前0 到k-1的位置
        self.reverse(nums, 0, k - 1)
        # 然后是K到n-1的位置
        self.reverse(nums, k, n - 1)
        return nums


if __name__ == '__main__':
    chen = Solution()
    print(chen.repeatedSubstringPattern(s))
