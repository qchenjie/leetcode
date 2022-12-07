# haystack = "bababadababac"
# needle = "ababad"
# haystack = "hello"
# needle = "ll"

haystack = ""
needle = ""

from typing import List


class Solution():
    def strStr(self, haystack: str, needle: str):
        i = 0
        j = 0
        n = len(haystack)
        b = len(needle)
        if b == 0 or n == 0:
            return 0
        nexts = self.get_nexts(needle)
        while i < n:
            if j >= b:
                break
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nexts[j]
        if j >= len(needle):
            return i - len(needle)
        else:
            return -1

    def get_nexts(self, needle: str) -> List[int]:
        n = len(needle)
        i = 0
        j = -1
        nexts = [0] * n
        nexts[0] = -1
        while i < n - 1:
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                nexts[i] = j
            else:
                j = nexts[j]
        return nexts


if __name__ == '__main__':
    chen = Solution()
    print(chen.strStr(haystack, needle))
