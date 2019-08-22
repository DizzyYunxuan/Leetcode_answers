#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
class Solution:
    def generateParenthesis(self, n: int):
        def generate(p, left, right, paras=[]):
            if left:
                generate(p+'(', left-1, right)
            if right > left:
                generate(p+')', left, right-1)
            if not right:
                paras += p,
            return paras
        return generate('', n, n)


# ✔ Accepted
#   ✔ 8/8 cases passed (36 ms)
#   ✔ Your runtime beats 93.96 % of python3 submissions
#   ✔ Your memory usage beats 6.67 % of python3 submissions (14 MB)


