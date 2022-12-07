# nums = [1, 3, 5, 2, 3, 3]
nums = [1, 3, 2, 2, 1]
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = [0] * n
        ret = []
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
            ret.append(max(left[i], right[i]))

        return sum(ret)


if __name__ == '__main__':
    chen = Solution()
    print(chen.candy(nums))
