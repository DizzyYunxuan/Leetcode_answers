#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        maxlength = 1
        nums = set(nums)
        for i in nums:
            if i - 1 not in nums:
                cur = i
                length = 1              
                while cur + 1 in nums:
                    cur += 1
                    length += 1
                maxlength = max(maxlength, length)
        return maxlength
✔ Accepted
  ✔ 68/68 cases passed (64 ms)
  ✔ Your runtime beats 80.26 % of python3 submissions
  ✔ Your memory usage beats 7.41 % of python3 submissions (15.2 MB)
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums = list(set(nums))
#         nums.sort()        
#         maxlength, length = 1, 1
#         i = 1
#         while i < len(nums):
#             if nums[i]-nums[i-1] == 1:
#                 length += 1
#                 maxlength = max(maxlength, length)
#             else:             
#                 length = 1
#             i += 1
#         return maxlength
# ✔ Accepted
#   ✔ 68/68 cases passed (64 ms)
#   ✔ Your runtime beats 80.26 % of python3 submissions
#   ✔ Your memory usage beats 7.41 % of python3 submissions (15.1 MB)

