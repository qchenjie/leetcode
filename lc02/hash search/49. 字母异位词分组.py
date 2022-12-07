# 二分查找
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            # Python不支持dict的key为list或dict类型，因为list和dict类型是unhashable（不可哈希）的。
            key = tuple(count)
            mp[key].append(st)

        print(mp)
        return list(mp.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st)) #你不join就变成了 key: [ 'a','e', 't ']
            mp[key].append(st)
        return list(mp.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    chen = Solution()
    print(chen.groupAnagrams1(strs))
