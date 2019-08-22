#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)
    ✔ Accepted
  ✔ 113/113 cases passed (32 ms)
  ✔ Your runtime beats 98.3 % of python3 submissions
  ✔ Your memory usage beats 6.06 % of python3 submissions (13.8 MB)
