words = ["bella", "label", "roller"]
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [0] * 26  # 不写成0乘以26的话下面的+=1就不行了，初始化又不是数字
        # 存着第一个单词的各个字符的频率
        for c in words[0]:
            min_freq[ord(c) - ord('a')] += 1
            # 找剩下的单词的频率
        for i in range(1, len(words)):
            freq = [0] * 26
            for c in words[i]:
                freq[ord(c) - ord('a')] += 1
            # 然后把剩下的单词和第一个单词比较，留住最小值，例如第一个单词的x出现了2次，但是其他的出现了0次
            for j in range(26):
                min_freq[j] = min(min_freq[j], freq[j])
        ans = list()
        # 这个题目这里也是个问题，他要重复的东西也加进去，下面这样的话就不是了

        # for i in range(26):
        #     if min_freq[i] > 0:
        #         ans.append(chr(i + ord('a')))
        for i in range(26):
            temp=chr(i + ord('a'))*min_freq[i]
            ans.extend(temp)

        return ans


if __name__ == '__main__':
    chen = Solution()
    print(chen.commonChars(words))
