#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
class Solution:
    def partition(self, s: str):
        self.res = []
        if not s:
            return 
        self.solver(s, [])
        return self.res

    def solver(self, s, path):
        if not s:
            self.res.append(path)
            return
        for window in range(len(s)):
            if self.isPalindrome(s[:window+1]):
                self.solver(s[window+1:], path+[s[:window+1]])
            # else:
            #     t = ' '.join(s[:window+1]).split()
            #     self.solver(s[window+1:], path+t)

    
    def isPalindrome(self, s):
        return s == s[::-1]
✔ Accepted
  ✔ 22/22 cases passed (96 ms)
  ✔ Your runtime beats 55.98 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (14 MB)
        
        


