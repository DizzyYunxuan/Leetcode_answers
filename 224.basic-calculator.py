#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
class Solution:
    def calculate(self, s: str) -> int:
        stack, i, cur = [], 0, ''
        while i < len(s):
            if cur == '+':
                stack.append(t)
                t = ''
            elif cur == '-':
                stack.append(t)
                t = '-'
            elif s[i] != ' ':
                cur += s[i]
            i += 1

        
if __name__ == "__main__":
    # res = Solution().calculate("(1+(4+5+2)-3)+(6+8)")
    res = Solution().calculate("2147483647")
            

