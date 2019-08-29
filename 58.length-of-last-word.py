#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
✔ Accepted
  ✔ 59/59 cases passed (32 ms)
  ✔ Your runtime beats 89.77 % of python3 submissions
  ✔ Your memory usage beats 5.26 % of python3 submissions (14 MB)
