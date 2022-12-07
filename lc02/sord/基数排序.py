class Solution():
    def radix_sort(self, s):
        """基数排序"""
        i = 0  # 例如 3453，取十位数的时候就是5,此时i等于2 就是记录当前取哪一位
        max_num = max(s)  # 最大值
        j = len(str(max_num))  # 记录最大值的位数,这里是6，345345
        while i < j:
            bucket_list = [[] for _ in range(10)]  # 初始化桶数组 [[], [], [], [], [], []]
            for x in s:
                # 例如取3435的十位的时候就是3435/10^1(先去掉5变成343)，然后再mod10得到3
                bucket_list[int(x / (10 ** i)) % 10].append(x)  # 找到位置放入桶数组,
            print(bucket_list)
            s.clear()
            for x in bucket_list:  # 放回原序列
                for y in x:
                    s.append(y)
            i += 1


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    chen = Solution()
    chen.radix_sort(a)
    print(a)
