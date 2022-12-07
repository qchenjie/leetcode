from typing import List

nums = [1, 2, 1, 3, 2, 5]
import collections
import operator

class Solution():
    def singleNumber(self, nums: List[int]) -> List[int]:
        idmap = {}
        ans = []
        test = set(nums)
        print(test)
        for i in nums:
            if i in idmap:
                idmap[i] += 1
            else:
                idmap[i] = 1
        for key in idmap.keys():
            if idmap[key] == 1:
                ans.append(key)
        return ans

    def singleNumber01(self, nums: List[int]) -> List[int]:
        idmap = {} # idmap : {'1':2, '2':2, '3': 1, '5': 1}
        ans = []
        for i in nums:
            if i in idmap:
                idmap[i] += 1
            else:
                idmap[i] = 1
        for value in idmap.values():
            ans.append(value)
        return ans

    def singleNumber02(self, nums: List[int]) -> List[int]:
        idmap = {}
        ans = []
        for i in nums:
            if i in idmap:
                idmap[i] += 1
            else:
                idmap[i] = 1
        for x, y in idmap.items():
            ans.append([x,y])
        return ans

    def singleNumber03(self, nums: List[int]) -> List[int]:
        idmap = {}
        ans = []
        for i in nums:
            if i in idmap:
                idmap[i] += 1
            else:
                idmap[i] = 1
        for x, y in idmap.items():
            if y ==1:
                ans.append(x)
        return ans

    def test_map(self):
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d = collections.defaultdict(list)
        for k, v in s:
            d[k].append(v)

        # Use dict and setdefault
        g = {}
        for k, v in s:
            g.setdefault(k, []).append(v)

        # Use dict 直接这样子用会覆盖的兄弟
        e = {}
        for k, v in s:
            e[k] = v

    # def test_map_sorted(self):
    #     classList = {"3" : ('john', 'A', 15),"2" : ('jane', 'B', 12), "1": ('dave', 'B', 10)}
    #
    #     sortedClassCount = sorted(classList.items(), key=operator.itemgetter(1), reverse=True)
    #     print(sortedClassCount)


if __name__ == '__main__':
    chen = Solution()
    print(chen.singleNumber01(nums))
