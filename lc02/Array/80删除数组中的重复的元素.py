# 删除数组中的重复的元素变形 leetcode80题
nums = [1, 1, 1, 2, 2, 3]


class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 1  # 始终要和i保持同步兄弟
        l = len(nums)
        repete = 0
        if l <= 2:
            return l
        for i in range(1, l):
            if nums[i] == nums[i - 1] and repete < 1:
                nums[k] = nums[i]
                k += 1
                repete+=1
            else:
                if nums[i] != nums[i - 1]:
                    nums[k] = nums[i]
                    k += 1
                    repete = 0;
        return k


if __name__ == '__main__':
    chen = Solution()
    chen.removeDuplicates(nums)
