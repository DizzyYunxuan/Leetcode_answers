#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
class Solution:
    def wordBreak(self, s: str, wordDict):
        if not s or not wordDict:
            return []
        self.shortest, self.longest, self.worddict = float('inf'), float('-inf'), wordDict
        for i in wordDict:
            self.shortest, self.longest = min(self.shortest, len(i)), max(self.longest, len(i))
        self.md = {len(s): ['']}
        # for i in range(len(res)):
        #     res[i] = res[i].strip()
        return list(map(lambda x: x.strip(), self.dfs(0, s)))
    
    def dfs(self, start, s):
        if start not in self.md:
            res = []
            for i in range(self.shortest, min(len(s)-start, self.longest)+1):
                if s[start:start+i] in self.worddict:
                    res.extend(list(map(lambda x: s[start:start+i]+' '+x, self.dfs(start+i, s))))
            self.md[start] = res
        return self.md[start]
✔ Accepted
  ✔ 39/39 cases passed (52 ms)
  ✔ Your runtime beats 77.07 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (14 MB) 
        
# if __name__ == "__main__":
#     s, wordDict = 'catsanddog', ["cat","cats","and","sand","dog"]
#     # s, wordDict = 'a', ['a']
#     res = Solution().wordBreak(s, wordDict)
#     print(res)

