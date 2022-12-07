# 计数排序适用于量大但是范围小的排序
class Solution():
    def countSort(self, nums):
        n = len(nums)
        output = [0] * n
        count=[0] * 10 # (0-9 有十个数字)这个是数字的范围，题目会告诉你范围的 他是统计频率的，例如1有几个，2有几个
        # [2, 4, 2, 7, 1, 1, 0, 0, 5, 6, 9, 8, 5, 7, 4, 0, 9]
        # [3, 2, 2, 0, 2, 2, 1, 2, 1, 2]
        # 然后输出3个0，两个1， 两个2


        for i in nums:
            count[i] += 1

        # 这他妈真的就是我自己的写的兄弟
        j = 0
        cnt = len(count)
        # 这里不能是 for i in range(n) 因为下面的count早就走完了 你还在那里搞事情会报错
        for i in range(cnt):
            while count[i]:
                output[j] = i
                count[i] -= 1
                j+=1
        return output

if __name__ == '__main__':
    nums = [2, 4, 2, 7, 1, 1, 0, 0, 5, 6, 9, 8, 5, 7, 4, 0, 9]
    chen = Solution()
    print(chen.countSort(nums))
