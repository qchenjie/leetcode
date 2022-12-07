s = "Let's take LeetCode contest"


class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        arr = list(s)
        left = 0
        while left < n:
            # 如果当前left不等于空格，否则就是看到下面的了else
            if arr[left] != " ":
                right = left
                while right + 1 < n and arr[right + 1] != " ":
                    right += 1
                self.reverseWord(arr, left, right)
                left=right+1

            else:
                left += 1
        return "".join(arr)

    # 下面这个一定要写的很熟练啊兄弟
    def reverseWord(self, arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1


if __name__ == '__main__':
    chen = Solution()
    print(chen.reverseWords(s))
