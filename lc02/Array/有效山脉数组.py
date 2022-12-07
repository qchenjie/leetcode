arr = [0, 3, 2, 1]

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n, i = len(arr), 0
         # 1. 找到最高点
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        #下面的是边界条件
        # 2. 判断：最高点不能是第一个和最后一个元素
        if i == 0 or i == n - 1:
            return False
        # 3. 从最高点往后递减扫描
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        # 4. 如果 i 指向数组最后一个元素，则返回 true，否则返回 false
        return i == n - 1


if __name__ == '__main__':
    chen = Solution()
    print(chen.validMountainArray(arr))
