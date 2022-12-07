from typing import List


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]：表示从位置[0, 0] 到 [i, j] 的路径数
        dp = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    # 状态压缩
    def uniquePaths01(self, m: int, n: int) -> int:
        dp = [-1] * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[j] = 1
                else:
                    dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 7
    # nums = [1, 2, 3, 1]
    print(solution.uniquePaths01(m, n))
