#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
✔ Accepted
  ✔ 34/34 cases passed (76 ms)
  ✔ Your runtime beats 55.23 % of python3 submissions
  ✔ Your memory usage beats 5.09 % of python3 submissions (15.2 MB)

