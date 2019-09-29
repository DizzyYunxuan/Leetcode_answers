#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zeros] = nums[zeros], nums[i]
                zeros += 1
✔ Accepted
  ✔ 21/21 cases passed (56 ms)
  ✔ Your runtime beats 85.07 % of python3 submissions
  ✔ Your memory usage beats 5.97 % of python3 submissions (15 MB)

    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 j = i + 1
#                 while j < len(nums):
#                     if nums[j] != 0:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break
#                     j += 1
#             i += 1
# ✔ Accepted
#   ✔ 21/21 cases passed (812 ms)
#   ✔ Your runtime beats 5.05 % of python3 submissions
#   ✔ Your memory usage beats 5.97 % of python3 submissions (15.2 MB)
        
                


