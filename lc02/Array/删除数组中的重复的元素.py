# 删除数组中的重复的元素


nums = [1, 1, 1, 2]


class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 1
        l = len(nums)
        if l == 1:
            return 1
        for i in range(1, l):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == '__main__':
    chen = Solution()
    chen.removeDuplicates(nums)
