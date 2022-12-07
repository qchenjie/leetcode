s = "4193 with words"


class Solution:
    def intToRoman(self, num: int) -> str:
        # 这里用两个数组维护，不然你用一个数组得开辟多大的空间啊
        # 然后就是用下面得组合表示整数
        # 例如799就是 500+299 299=100+199 然后这样分下去
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res = ''
        for index in range(13):
            # 第一次找到了500  然后扎到了100，然后又找到了100
            while num >= nums[index]:
                res += romans[index]
                num -= nums[index]

        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.intToRoman(799))
