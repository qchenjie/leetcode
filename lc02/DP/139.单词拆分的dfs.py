from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        memo = {}

        def dfs(i):
            # 递归终止条件
            # 这里i可以是5，如果能走到5，说明有这条路径，不然中间就剪枝掉了
            if i == n:
                return True
            if i in memo:
                return memo[i]
            # 迭代每一个根的子节点
            for end in range(i + 1, n + 1):
                # 先判断根节点，提前剪枝
                if s[i:end] not in wordDict:
                    continue
                    # 我还是return False，还是欠缺了火候，直接return false的话，
                    # return False
                flag = dfs(end)
                # 只有有一个flag是true都返回了
                if flag:
                    memo[i] = True
                    return True
            # 没有一个flag是ture的
            memo[i] = False
            return False
        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    s = "douma"
    wordDict = ["dou", "ma"]
    print(solution.wordBreak(s, wordDict))
