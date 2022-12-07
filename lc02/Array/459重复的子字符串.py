s = "aabaaba"


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        # 循环长度
        for lenstr in range(1, n // 2 + 1):
            if n % lenstr == 0:
                i = 0
                matched = True
                for j in range(lenstr, n):
                    if s[i] != s[j]:
                        matched = False
                        break
                    else:
                        i += 1
                if matched:
                    return True
        return False


if __name__ == '__main__':
    chen = Solution()
    print(chen.repeatedSubstringPattern(s))
