from typing import List


nums = [1,8,6,2,5,4,8,3,7]
# nums = [1, 1]

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        if len(height)==2:
            return min(height[0],height[1])
        else:
            for i in range(len(height) - 2):
                for j in range(i + 1, len(height)):
                    curr_area = (j - i) * min(height[i], height[j])
                    if curr_area > max_area:
                        max_area = curr_area
        return max_area


if __name__ == '__main__':
    chen = Solution()
    print(chen.maxArea(nums))
