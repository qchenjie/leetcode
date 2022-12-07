# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right = x
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == '__main__':
    # 这玩意必须要有序
    a = [1, 2, 3, 4, 8, 21, 78, 78, 78, 78, 79, 81, 92, 108]
    target = 7
    chen = Solution()
    print(chen.mySqrt(target))
