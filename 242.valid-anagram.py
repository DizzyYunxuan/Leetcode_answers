#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
✔ Accepted
  ✔ 34/34 cases passed (44 ms)
  ✔ Your runtime beats 93.1 % of python3 submissions
  ✔ Your memory usage beats 9.38 % of python3 submissions (14.1 MB)
