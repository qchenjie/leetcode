# 二分查找
from typing import List

s = "egd"
t = "adg"

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for sc, tc in zip(s, t):
            # ('e', 'a'), ('g', 'd'), ('d', 'g')
            # if s2t.get(sc, tc) != tc or t2s.get(tc, sc) != sc:
            if ((sc in s2t and s2t[sc] != tc) or (tc in t2s and t2s[tc] != sc)):
                return False
            s2t[sc], t2s[tc] = tc, sc
        return True


if __name__ == '__main__':
    chen = Solution()
    print(chen.isIsomorphic(s, t))
