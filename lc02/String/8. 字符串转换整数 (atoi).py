s = "4193 with words"


class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        i = 0
        # 先去掉空格
        while i < n and s[i] == ' ':
            i += 1
        # 确定符号是正号还是负号,这里只看首位,
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        INT_MAX = 2 ** 31 - 1  # -2147483648
        INT_MIN = -2 ** 31  # 2147483647
        base = 0
        # 只有是数字的时候
        while i < n and '0' <= s[i] <= '9':
            # 下面要*10 ,因为要先判断一下越界没有，INT_MAX //10 是取整数，2147483647取完整数就剩下7了所以下面是判断7
            if (base > INT_MAX // 10 or (base == INT_MAX // 10 and ord(s[i]) - ord('0') > 7)):
                # 都已经超过了范围了，所以直接的截断
                if sign > 0:
                    return INT_MAX
                else:
                    return INT_MIN

            base = base * 10 + ord(s[i]) - ord('0')
            i += 1
        return sign * base


if __name__ == '__main__':
    chen = Solution()
    print(chen.myAtoi(s))
