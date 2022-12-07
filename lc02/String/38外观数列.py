n = 4


class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        # 这个for循环是用来计算1 2 3 4 你要算4，就是从1开始一个个开始计算
        for i in range(1, n):
            # prev初始化,prev都是等于curr的然后curr等于下一个
            prev = curr
            # 要重置那个格式
            curr = ""
            say = prev[0]
            count = 1
            # 这个for循环是 假如算到了3，通过循环3算4这样的
            for j in range(1, len(prev)):
                if prev[j] == say:
                    count += 1

                else:
                    curr += str(count)
                    curr += say
                    say = prev[j]
                    # 重置count
                    count = 1
            # 把数量和字符都统计好写好,上面也有下面两句话，下面的是循环退出了，然后拼接最后一个字符串用的
            curr += str(count)
            curr += say
        return curr


if __name__ == '__main__':
    chen = Solution()
    print(chen.countAndSay(n))
