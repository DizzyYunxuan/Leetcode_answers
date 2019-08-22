#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack, l = [], len(s)
        for i in range(l):
            stack.append(s[i])
            if len(stack) > 1 and (stack[-2]+stack[-1] == '()' 
            or stack[-2]+stack[-1] == '{}' 
            or stack[-2]+stack[-1] == '[]'):
                stack.pop()
                stack.pop()
        if stack:
            return False
        else:
            return True
# ✔ Accepted
#   ✔ 76/76 cases passed (24 ms)
#   ✔ Your runtime beats 99.82 % of python3 submissions
#   ✔ Your memory usage beats 5.04 % of python3 submissions (13.6 MB)

