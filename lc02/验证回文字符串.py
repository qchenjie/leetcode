class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # 如果现在左边的出现了无效字符
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # 判断当前字符(全都转成小写再判断)
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    # s = "a+b-a"
    s = "ab(%BA"
    chen = Solution()
    print(chen.isPalindrome(s))
