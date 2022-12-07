# 二分查找
class Solution():
    # 迭代实现
    def BasicBinarySearch(self, nums, target):
        """二分查找"""
        if nums == None or len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # 递归实现
    def BasicBinarySearchR(self, nums, left, right, target):
        if left > right:
            return False
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if target < nums[mid]:
            return self.BasicBinarySearchR(nums, left, mid - 1, target)
        else:
            return self.BasicBinarySearchR(nums, mid + 1, right, target)


if __name__ == '__main__':
    # 这玩意必须要有序
    # a = [1, 2, 3, 4, 8, 21, 34, 45, 56, 78, 79, 81, 92, 108]
    a = [1, 2]
    target = 78
    chen = Solution()
    print(chen.BasicBinarySearch(a, target))
