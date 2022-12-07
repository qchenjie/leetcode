from typing import List

nums = [1, 2, 3, 4]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        output[0] = 1  # 第一个左边就是1
        # 从第二个开始更新
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]
        # 更新右边的，右边的是从右往前走，python 的骚操作
        # 逆序输出-1 到 n-1这里，依然遵循左开右闭的 -1的不输出
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * right_product;
            right_product *= nums[i]
        return output


if __name__ == '__main__':
    chen = Solution()
    print(chen.productExceptSelf(nums))
