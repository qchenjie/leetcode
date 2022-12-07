# 二分查找
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        currNuM = 1
        MissCnt = 0
        lastMissNum = -1

        i = 0
        while MissCnt < k:
            # if i>=len(arr):
            #     break
            if currNuM == arr[i]:
                if i < len(arr)-1:
                    i += 1
            else:
                MissCnt += 1
                lastMissNum = currNuM
            currNuM += 1
        return lastMissNum

    def findKthPositive01(self, arr: List[int], k:int) -> int:
        if arr[0] > k:
            return k
        n = len(arr)
        left = 0
        right = n  # 这里的细节是right = n而不是n-1
        # 先计算第i个元素前面缺失元素的个数
        nums=[0] * n
        for i in range(n):
            nums[i] = arr[i] - i -1

        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < k:
                left = mid +1
            else:
                right = mid
        return arr[left-1] + (k-nums[left-1] )


if __name__ == '__main__':
    # 这玩意必须要有序
    nums = [1, 3]
    target = 1
    chen = Solution()
    print(chen.findKthPositive01(nums, target))
