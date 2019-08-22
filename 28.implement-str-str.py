#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i+len(needle)] == needle:
                return i       
        return -1

✔ Accepted
  ✔ 74/74 cases passed (32 ms)
  ✔ Your runtime beats 94.21 % of python3 submissions
  ✔ Your memory usage beats 12.31 % of python3 submissions (14 MB)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
