from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态定义
        # dp[i][j] 表示第 i 天处于状态 j 获取到的最大利益
        # 其中 j 可以取值为： 0 表示不持股；1 表示持股

        # 每只股票都有卖或者不卖两种状态，所以是n行，两列
        dp = [[0] * 2 for _ in range(len(prices))]

        # 第0天，不买就是0，买了就是负债
        dp[0][0], dp[0][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])

        # 返回的不是dp[len(prices) - 1][1] 因为1是买股票，是负债
        return dp[len(prices) - 1][0]

    def maxProfit01(self, prices: List[int]) -> int:

        dp = [0] * 2

        # 第0天，不买就是0，买了就是负债
        dp[0] = 0
        dp[1] = -prices[0]

        for i in range(1, len(prices)):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], -prices[i])

        # 返回的不是dp[len(prices) - 1][1] 因为1是买股票，是负债
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    price = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(price))
