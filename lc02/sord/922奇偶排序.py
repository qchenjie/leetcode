# nums = [4, 2, 5, 7]
nums = [2, 3, 0, 0]
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        n = len(A)
        arr = [0] * n
        for a in A:
            if i<n and a % 2 == 0:
                arr[i] = a
                i += 2
        i = 1
        for a in A:
            if i<n and a % 2 == 1:
                arr[i] = a
                i += 2
        return arr


if __name__ == '__main__':
    chen = Solution()
    print(chen.sortArrayByParityII(nums))
