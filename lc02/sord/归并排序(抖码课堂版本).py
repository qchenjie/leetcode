from typing import List

nums = [8, 4, 5, 7, 1, 3, 6, 2]
# nums = [0]

class Solution:
    def merge_sort(self, nums, lo, hi, tmp) -> List[int]:
        len_nums = len(nums)
        if len_nums == 1:
            return nums
        elif lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.merge_sort(nums, lo, mid, tmp)
        self.merge_sort(nums, mid + 1, hi, tmp)
        # 递归不要进去了，左右两边都拍好了，就剩下下面的合并了
        self.merge(nums, lo, mid, hi, tmp)
        return nums

    def merge(self, nums, lo, mid, hi, tmp) -> None:
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


if __name__ == '__main__':
    chen = Solution()
    # 这里一定是temp等于全部的数组的大小，否则就是不健壮了
    tmp = [0] * len(nums)
    print(chen.merge_sort(nums, 0, len(nums) - 1, tmp))
