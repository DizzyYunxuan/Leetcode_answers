#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        zp, res = zip(*strs), ''
        for i in zp:
            if len(set(i)) > 1:
                break
            res += i[0]
        return res

#     ✔ Accepted
#   ✔ 118/118 cases passed (36 ms)
#   ✔ Your runtime beats 90.71 % of python3 submissions
#   ✔ Your memory usage beats 5.31 % of python3 submissions (13.8 MB)

