#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.myMatch(s, len(s)-1, p, len(p)-1)
    
    def myMatch(self, s, i, p, j):
        if j == -1 and i == -1:
            return True
        elif j == -1 and i != -1:
            return False
        
        if p[j] == '*':
            

                

# if __name__ == '__main__':
#     res = Solution().isMatch('aaa', 'ab*a*c*a')
#     print(res)
