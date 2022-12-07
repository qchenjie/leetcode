class Solution:
    # 1. 记忆化搜索(一)
    def rob1(self, nums) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i) -> int:
            if i >= n: return 0
            if memo[i] != -1: return memo[i]
            left = dfs(i + 1)
            right = dfs(i + 2)
            memo[i] = max(left, right + nums[i])
            return memo[i]

        return dfs(0)


        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 9, 3, 1]
    print(solution.rob1(nums))
