class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return
        n = len(s)
        if n == 1:
            return 1
        res = 0
        for i in range(n):
            for j in range(i, n):
                chen = s[i:j+1]
                if self.ishuiwen(chen):
                    res += 1
        return res

    def ishuiwen(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "aba"
    print(solution.countSubstrings(s))
