# 二分查找
from typing import List

# pattern = "abba"
# str = "dog cat cat dog"

pattern = "abba"
str = "dog cat cat fish"


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char2Word, word2Char = {}, {}
        for c, word in zip(pattern, words):
            # 下面要表达的意思是如果key在那个地方，且value不是对应的value，那就直接gg
            # char2Word是用s的作为Key ,word2Char是用t做的的key
            if ((c in char2Word and char2Word[c] != word)
                    or (word in word2Char and word2Char[word] != c)):
                return False
            char2Word[c], word2Char[word] = word, c
        return True


if __name__ == '__main__':
    chen = Solution()
    print(chen.wordPattern(pattern, str))
