#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words) -> int:
        length, res = {}, 0
        for word in words:
            biword = 0
            for c in word:
                biword |= 1 << ord(c) - 97
            curlen = length.get(biword, 0)
            if len(word) > curlen:
                res = max(res, len(word)*max([0]+[length[i] for i in length if not i & biword]))
                length[biword] = len(word)
        return res

Accepted
174/174 cases passed (188 ms)
Your runtime beats 96.04 % of python3 submissions
Your memory usage beats 25 % of python3 submissions (14 MB)
# if __name__ == "__main__":
#     res = Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
# @lc code=end

