#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.56%)
# Likes:    5789
# Dislikes: 330
# Total Accepted:    987.8K
# Total Submissions: 3.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         lss, start,worker, lens= '', 0, 0, 0
#         while start <= len(s) - 1 and worker <= len(s) - 1:
#             if s[worker] not in lss:
#                 lss += s[worker]
#                 worker += 1
#                 if len(lss) > lens:
#                     lens = len(lss)
#             else:
#                 if len(lss) > lens:
#                     lens = len(lss)
#                 idx = lss.index(s[worker])
#                 start = start+ idx +1
#                 worker = start
#                 lss = ''
#         return lens

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic , start, res = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)

