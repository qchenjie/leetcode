
from typing import List

# 下面的题目是自己写的，但是我一直毛病
# wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
# wall = [[1],[1],[1]]
wall = [[79,12,208,1]]
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # edge[i]表示第i个数字的边缘，
        edge_map = {}
        for nums in wall:
            n = len(nums)
            edge = [0] * n
            for i in range(1, n):
                edge[0] = nums[0]
                edge[i] = edge[i - 1] + nums[i]
            for c in edge:
                if c in edge_map:
                    edge_map[c] += 1
                else:
                    edge_map[c] = 1

        # 找出edge_map中value第二大的那个：(想一想阿里面试题)
        edge_map_list = edge_map.values()
        if len(edge_map_list) == 1:
            return len(wall)
        else:
            edge_map_list = sorted(edge_map_list)
            return len(wall) - edge_map_list[-2]


if __name__ == '__main__':
    chen = Solution()
    print(chen.leastBricks(wall))
