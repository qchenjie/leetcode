# 二分查找

class Solution():
    # 原理实现
    def FirstTargetElemnts(self, nums, target):
        """查找第─个大于等于目标值的元素"""
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 如果当前的等于target,还要再判断一下前面是否小于，小于，这就是第一个
                # 如果也是大于，那前面的相当于还有，直接把right放到mid-1中去
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            # 等于和大于的逻辑是一样的，所以可以合并，看下面的
            elif nums[mid] > target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

    # 简洁版本

    def FirstTargetElemnts01(self, nums, target):
        """查找第─个大于等于目标值的元素"""
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                # 如果当前的等于target,还要再判断一下前面是否小于，小于，这就是第一个
                # 如果也是大于，那前面的相当于还有，直接把right放到mid-1中去
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            # 等于和大于的逻辑是一样的，所以可以合并，看下面的
            else:
                left = mid + 1


if __name__ == '__main__':
    # 这玩意必须要有序
    a = [1, 2, 3, 4, 8, 21, 78, 78, 78, 78, 79, 81, 92, 108]
    target = 50
    chen = Solution()
    print(chen.FirstTargetElemnts01(a, target))
