from typing import List

nums = [3, 30, 34, 5, 9]


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        chen = []
        for i in nums:
            chen.append(str(i))
        largest_num = ''.join(sorted(chen, key = LargerNumKey))
        return "0" if largest_num[0] == '0' else largest_num



if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber(nums))
