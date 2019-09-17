#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item == '+':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 + n2)
            elif item == '-':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 - n2)
            elif item == '*':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(n1 * n2) 
            elif item == '/':
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                stack.append(int(n1 / n2))
            else:
                stack.append(item)
        return stack[0] 
✔ Accepted
  ✔ 20/20 cases passed (76 ms)
  ✔ Your runtime beats 83.37 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (14.2 MB)
