nums = [4, 3, 2, 7, 8, 2, 3, 1]
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        lenth = len(nums)
        index = 0  # for i in nums 要用索引不能像前面的这样，我还要判断值等不等于索引呢
        while index < lenth:
            if nums[index] == index + 1:  # 如果值等于索引
                index += 1
            else:
                targetindex = nums[index] - 1  # 值和索引之前差一个1
                if nums[targetindex] == nums[index]:  # 如果有重复的元素（意思就是当前值作为索引的位置的值已经是对的了）
                    index += 1
                    continue
                    # 否则就直接交换一下
                nums[targetindex], nums[index] = nums[index], nums[targetindex]  # 交换一下，python的交换独具特色
        for i in range(lenth):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.findDisappearedNumbers(nums))
