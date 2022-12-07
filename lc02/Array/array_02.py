nums = [0, 1, 0, 3, 12]

class Solution:
    def moveZeroes(self,nums) -> None:
        # 转化成移除所有0元素的
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        print(index)

        while index<len(nums):
            nums[index] = 0
            index+=1
        print(nums)


if __name__=='__main__':
    chen=Solution()
    chen.moveZeroes(nums)