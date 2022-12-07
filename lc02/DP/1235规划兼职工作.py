class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:

        # 先计算prev[i] 表示选了i之后前面最近能选谁

        n = len(startTime)

        pre = [-1] * (n+1)

        # range(5,0,-1)倒序输出 [1,2,3,4,5]，注意这里的(5,0,-1)也是遵循前闭后开的原则，即不输出0。
        for i in range(n - 1, 0, -1):
            last = startTime[i]  # 3 ,例如这里最晚是3
            for j in range(i - 1, -1, -1):
                # 如果他的最晚时间等于后面的最早时间
                if endTime[j] <= startTime[i]:
                    pre[i] = j
                    break

        def opt(n):
            if n == 1:
                return profit[0]
            if n == 0:
                return 0
            return max(opt(n-1), profit[n]+opt(pre[n]))

        return opt(n)


if __name__ == '__main__':
    solution = Solution()
    startTime = [1, 2, 3, 4, 6]
    endTime = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    print(solution.jobScheduling(startTime, endTime, profit))
