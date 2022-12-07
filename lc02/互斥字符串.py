class Solution:
    def minDistance(self, word1: str) -> int:
        n = len(word1)
        word2 = ["AB"]*n
        word2 = word1.join()
        m = len(word2)


        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(down, left_down)

        return D[n][m]


if __name__ == '__main__':
    solution = Solution()
    word1 = "AABAAAB"
    word2 = "ABABABA"
    print(solution.minDistance(word1))
