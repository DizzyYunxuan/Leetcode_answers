#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str):
        self.depth = float('inf')
        self.d = {}
        self.res = []
        self.dfs(s, 0)
        return self.res

    def dfs(self, s, depth):     
        if depth > self.depth:
            return
        if s in self.d:
            return
        else:
            self.d[s] = True

        if self.isOK(s):
            if depth == self.depth:
                self.res.append(s)
            elif depth < self.depth:
                self.res = [s]
                self.depth = depth
       
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                continue
            if s[i] in '()':
                self.dfs(s[:i] + s[i+1:], depth+1)

    def isOK(self, s):
        if not s:
            return True
        stack = []
        for i in s:
            if i == ')':
                if not stack:
                    return False
                if stack[-1] == '(':
                    stack.pop()
            elif i in '()':
                stack.append(i)
        return not stack
Accepted
126/126 cases passed (356 ms)
Your runtime beats 22.8 % of python3 submissions
Your memory usage beats 10.53 % of python3 submissions (14.7 MB)
# if __name__ == "__main__":
#      res = Solution().bfs("()())()")



# @lc code=end

