# s="chen hao rong"
# s=list(s)
# print(s)
#
# s[0]='x'
# print(s)
# print(''.join(s))

#
# i = 13
# print(i / 5)
# print(i // 5)

# 判断大小写

# s = "zhZn#$haorong9110"
#
#
# class Solution():
#     def isalpha(self, s: str) -> str:
#         c = []
#         for i in s:
#             if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or '0'<= i <= '9':
#                 c.append(i)
#         return ''.join(c)
#
#
# if __name__ == '__main__':
#     chen = Solution()
#     print(chen.isalpha(s))




s = "1233456"
num=[1, 2, 3, 4, 5, 6]

class Solution():
    def alphatonum(self, s: str) -> int:
        c = list(s)
        return ''.join(c)+1
# 上面的不行，要下面这样的  # 字符串转数字
    def alphatonum01(self, s: str) -> int:
        base=0
        for i in s:
            base=base*10+ord(i)-ord('0')
        return base
# 字符串转数字
    def numtostr(self,num:int):
        chen = []
        for i in num:
            chen.append(str(i))
        return chen

# 测试float('inf')
    def printfloat_inf(self):
        print(float('inf'))


if __name__ == '__main__':
    chen = Solution()
    #print(chen.alphatonum01(s))
    print(chen.printfloat_inf())




