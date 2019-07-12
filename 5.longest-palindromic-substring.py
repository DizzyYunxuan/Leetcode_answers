#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.54%)
# Likes:    3850
# Dislikes: 368
# Total Accepted:    592.4K
# Total Submissions: 2.2M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# Naive method

class Solution:
    def longestPalindrome(self, s: str) -> str:  
        center, length, longest, lps = 1, 0, 0, ''
        if len(s) == 0 or len(s) == 1: 
            lps = s
            return lps
        elif len(s) == 2 and s[0] == s[1]:
            return s
        elif len(s) == 2 and s[0] != s[1]:
            return s[0]
        while center < len(s) - 1:
            length = 0
            if s[center] == s[center - 1]:
                i, j = center - 1, center
                length = 0
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    i, j = i - 1, j + 1
                    length += 2
                if length > longest:
                    lps = s[i+1:j]
                    longest = length
            if s[center-1] == s[center+1]:
                i, j = center - 1, center + 1
                length = 1
                while i >= 0 and j < len(s) and s[i] == s[j]:
                    i, j = i - 1, j + 1
                    length += 2     
                if length > longest:
                    lps = s[i+1:j]
                    longest = length            
            center += 1
        if longest < 2:
            if s[center] == s[center-1]:
                lps = s[center-1: center+1]
            else:
                return s[0]
            
        return lps      

# ✔ Accepted
#   ✔ 103/103 cases passed (1024 ms)
#   ✔ Your runtime beats 60.43 % of python3 submissions
#   ✔ Your memory usage beats 55.81 % of python3 submissions (13.2 MB)




# Dynamic Program 

# class Solution:
#     def longestPalindrome(self, s: str) -> str: 
#         length, longest, lps = len(s), 0, ''
#         if length == 0:
#             return lps
#         DPT = [[0 for i in range(length)] for j in range(length)]
#         for j in range(length):
#             DPT[j][j] = 1
#             i = 0
#             for i in range(i, j+1):
#                 if s[i]==s[j] and (j-i<2 or j>0 and DPT[i+1][j-1]) :
#                     DPT[i][j] = 1
#                 if DPT[i][j] and j-i+1 > longest:     
#                     longest = j - i + 1         
#                     lps = s[i:j+1]
                
#         return lps

# ✔ Accepted
#   ✔ 103/103 cases passed (4012 ms)
#   ✔ Your runtime beats 30.05 % of python3 submissions
#   ✔ Your memory usage beats 10.65 % of python3 submissions (21.8 MB)


# if __name__ == '__main__':
#     a = Solution().longestPalindrome('cbbd')
#     print(a)


