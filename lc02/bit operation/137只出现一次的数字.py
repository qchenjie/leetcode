nums = [3, 3, 6, 3]
# 3:0011
# 3:0011
# 3:0011
# 6:0110
#   0143(看每一位有几个1，
#   0110  是3的倍数设置为0，其余为1
# 0110转成10进制就是6


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            one_count = sum((num >> i) & 1 for num in nums)
            if one_count % 3:
                # Python 这里对于最高位需要特殊判断
                if i == 31:
                    res -= (1 << i)
                else:
                    res |= (1 << i)
        return res


if __name__ == '__main__':
    chen = Solution()
    print(chen.singleNumber(nums))
