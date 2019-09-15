#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # dp = [0] * (len(s) + 1)
        sli = [0]
        for i in range(len(s)+1):
            for start in sli:
                if s[start:i] in wordDict:
                    sli.append(i)
                    break
        return True if sli[-1] == len(s) else False
✔ Accepted
  ✔ 36/36 cases passed (48 ms)
  ✔ Your runtime beats 53.32 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     s, worddict = "leetcode", ["leet","code"]
#     res = Solution().wordBreak(s, worddict)
#     print(res)
