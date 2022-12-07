from typing import List

nums = [7, 5, 6, 4]


class Solution:
    def merge_sort(self, nums, lo, hi, tmp) -> int:
        if lo >= hi:
            return 0
        mid = lo + (hi - lo) // 2
        left = self.merge_sort(nums, lo, mid, tmp)
        right = self.merge_sort(nums, mid + 1, hi, tmp)
        mergeSortCount = self.merge(nums, lo, mid, hi, tmp)
        return left + right + mergeSortCount

    def merge(self, nums, lo, mid, hi, tmp) -> int:
        # 把nums的值拷贝到temp中
        for i in range(lo, hi + 1):
            tmp[i] = nums[i]

        i, j, count = lo, mid + 1, 0

        for k in range(lo, hi + 1):
            # 左边走完了 ，直接把右边的复制过来
            if i == mid + 1:
                nums[k] = tmp[j]
                j = j + 1
            # 右边走完了 ，直接把左边的复制过来
            elif j == hi + 1:
                nums[k] = tmp[i]
                i = i + 1
            # 然后就是合并的过程
            elif tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i = i + 1
            else:
                nums[k] = tmp[j]
                j = j + 1
                count += (mid - i + 1)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        tmp = [0] * len(nums)
        return self.merge_sort(nums, 0, len(nums) - 1, tmp)


if __name__ == '__main__':
    chen = Solution()
    print(chen.reversePairs(nums))
