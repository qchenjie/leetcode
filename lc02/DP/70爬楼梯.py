from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            left = dfs(n - 1)
            right = dfs(n - 2)
            return left + right

        return dfs(n)


if __name__ == '__main__':
    solution = Solution()

    print(solution.climbStairs(5))
