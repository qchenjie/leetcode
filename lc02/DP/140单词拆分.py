from typing import List

class Solution:
    # 回溯
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = set(wordDict)

        def dfs(i) -> List[str]:
            res = []
            if i == len(s):
                res.append("")
                return res

            for end in range(i + 1, len(s) + 1):
                if s[i:end] not in word_dict: continue
                strings = dfs(end)
                for string in strings:
                    # split = "" if string == "" else " "
                    split = " "
                    res.append(s[i:end] + split + string)
            return res

        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(solution.wordBreak(s, wordDict))
