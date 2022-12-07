from typing import List


# 二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        # 比较对角线上的次数
        shortDim = min(m, n)
        for i in range(shortDim):
            # 这里不用把当前位置的二维坐标传进去，因为行列是分开的
            rowFound = self.binarySearchRow(matrix, i, target)
            colFound = self.binarySearchcol(matrix, i, target)
            if rowFound or colFound:
                return True
        return False

    def binarySearchRow(self, matrix, row, target):
        lo = row
        hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

    def binarySearchcol(self, matrix, row, target):
        lo = row
        hi = len(matrix) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if matrix[mid][row] == target:
                return True
            elif matrix[mid][row] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == '__main__':
    # 这玩意必须要有序
    # a = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    a = [[5],[6]]
    target = 6
    chen = Solution()
    print(chen.searchMatrix(a, target))
