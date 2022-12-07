# 二分查找

class Solution():
    # 原理实现
    def LastTargetElemnts(self, nums, target):
        """查找最后一个小于等于目标值的元素"""
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 如果当前的等于target,还要再判断一下后面是否大于，大于，这就是最后一个
                # 如果也是小于，那后面的相当于还有，直接把left放到mid+1中去
                if mid == len(nums) or nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
            # 等于和小于的逻辑是一样的，所以可以合并，看下面的
            # 如果当前元素小于
            elif nums[mid] < target:
                # 如果当前元素小于，并且，后一个元素大于，那这就是最后一个
                if mid == len(nums) or nums[mid + 1] > target:
                    return mid
                # 否则后面还有小的
                else:
                    left = mid + 1
            # 这个否则就是当前元素大于target
            else:
                right = mid - 1

    # 简洁版本

    def LastTargetElemnts01(self, nums, target):
        """查找最后一个小于等于目标值的元素"""
        if nums == None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                # 如果当前的等于target,还要再判断一下后面是否大于，大于，这就是最后一个
                # 如果也是小于，那后面的相当于还有，直接把left放到mid+1中去
                if mid == len(nums) or nums[mid + 1] > target:
                    return mid
                else:
                    left = mid + 1
            # 等于和小于的逻辑是一样的，所以可以合并，看下面的
            else:
                right = mid - 1


if __name__ == '__main__':
    # 这玩意必须要有序
    a = [1, 2, 3, 4, 8, 21, 78, 78, 78, 78, 80, 81, 92, 108]
    target = 50
    chen = Solution()
    print(chen.LastTargetElemnts01(a, target))
