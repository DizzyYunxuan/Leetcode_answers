#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            try:
                stack.remove(n)
            except:
                stack.append(n)
        return stack
✔ Accepted
  ✔ 30/30 cases passed (688 ms)
  ✔ Your runtime beats 5.19 % of python3 submissions
  ✔ Your memory usage beats 50 % of python3 submissions (15.5 MB)
