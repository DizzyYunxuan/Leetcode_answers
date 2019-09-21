#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        def helper(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        return ''.join(sorted(map(str, nums), key=cmp_to_key(helper))).lstrip('0') or '0'
✔ Accepted
  ✔ 222/222 cases passed (48 ms)
  ✔ Your runtime beats 58.64 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (14 MB)
