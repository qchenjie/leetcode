coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0][0], coordinates[0][1]
        x, y = coordinates[1][0], coordinates[1][1]
        # k=(y-y0)/(x-x0)
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i][0], coordinates[i][1]

            return (y - y0) * (xi - x0) == (yi - y0) * (x - x0)
        return True


if __name__ == '__main__':
    chen = Solution()
    print(chen.checkStraightLine(coordinates))
