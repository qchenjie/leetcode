s = 123


class Solution:
    def reverse(self, x: int) -> int:
        left = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        x = str(x)
        x = list(x)
        right = len(x) - 1
        if x[left] < '0' or x[left] > '9':
            left += 1
        while left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
        # 然后拼接起来
        INT_MAX = 2 ** 31 - 1  # -2147483648
        INT_MIN = -2 ** 31  # 2147483647
        i = 0
        base = 0
        while i < len(x):
            if (base > INT_MAX // 10 or (base == INT_MAX // 10 and ord(x[i]) - ord('0') > 7)):
                return 0
            base = base * 10 + ord(x[i]) - ord('0')
            i+=1
        return sign * base


if __name__ == '__main__':
    chen = Solution()
    print(chen.reverse(s))
