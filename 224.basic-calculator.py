#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
class Solution:
    def calculate(self, s: str) -> int:
        res, signs = 0, [1, 1]
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return res
✔ Accepted
  ✔ 37/37 cases passed (152 ms)
  ✔ Your runtime beats 34.59 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (15.2 MB)
        
# if __name__ == "__main__":
#     # res = Solution().calculate("(1+(4+5+2)-3)+(6+8)")
#     res = Solution().calculate("(1+(4+5+2)-3)+(6+8)")
            

