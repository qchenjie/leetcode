s = 10


class Solution:
    def countPrimes(self, n: int) -> int:
        ans = 0
        not_primes = [False] * n
        for x in range(2, n):
            # 如果已经标明了不是质数就continue
            if not_primes[x]:
                continue
            # 否则就加一，同时用下面的循环标记
            ans += 1
        # 如果 x 是质数，那么 2x、3x、4x.... 肯定不是质数
        # 说明：这里 i 最好是从 x + x 开始，因为 x 有可能是质数
        # 其实 i 从 x 开始也没啥问题，因为 x 在上面已经判断过了
        # 但是，这样就违背了 notPrimes 数组的含义了，所以这里修改为 x + x
        #第三个空是每X个数字跳过
            for i in range(x + x, n, x):
                not_primes[i] = True
        return ans


if __name__ == '__main__':
    chen = Solution()
    print(chen.countPrimes(s))
