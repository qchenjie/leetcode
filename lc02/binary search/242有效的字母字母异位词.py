# 二分查找
from typing import List

s = "anaaram"
t = "nagaram"


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        # 先记录s = {"a":3, "n":1, "g":1, "r":1, "m":1}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        # 然后去t中去看，这一段代码我真的是写不出来卧槽
        # 假设s中a出现2次，t中a出现了1次
        for c in t:
            if not c in count or count[c] <= 0:
                return False
            count[c] -= 1
        return True

    def isAnagram01(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        # count_s: {'a ' : 4 ,'n ' : 1, 'r ' : 1,'m ' : 1}
        for c in s:
            if c in count_s:
                count_s[c] += 1
            else:
                count_s[c] = 1
        # count_t: {'a ' : 4 ,'n ' : 1, 'r ' : 1,'m ' : 1}
        for c in t:
            if c in count_t:
                count_t[c] += 1
            else:
                count_t[c] = 1

    # 然后呢？ 怎么比较两个字典


if __name__ == '__main__':
    chen = Solution()
    print(chen.isAnagram01(s, t))
