# 二分查找
class Solution():
    # 迭代实现
    def LastTargetElemnts(self, nums, target):
        """查找最后一个等于目标值的元素"""
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 如果当前的等于target,还要再判断一下后面一个是否等于，如果不等于，这就是最后一个
                # 如果等于，那后面的相当于还有，直接把left放到mid+1中去
                if mid == len(nums)-1 or nums[mid + 1] != target:
                    return mid
                else:
                    left = mid + 1
            # 这里要改的就是在等于那里判断一下。其他的不等于就不用动了
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    # 这玩意必须要有序
    a = [1, 2, 3, 4, 8, 21, 78, 78, 78, 78, 79, 81, 92, 108]
    target = 78
    chen = Solution()
    print(chen.LastTargetElemnts(a, target))
