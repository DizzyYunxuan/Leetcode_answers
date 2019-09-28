#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, opt in enumerate(input):
            if opt in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.cal(l, r, opt))
        return res

    def cal(self, x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        else:
            return x * y
✔ Accepted
  ✔ 25/25 cases passed (36 ms)
  ✔ Your runtime beats 92.73 % of python3 submissions
  ✔ Your memory usage beats 11.11 % of python3 submissions (13.9 MB)

    

