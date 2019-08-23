#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        i, n1, n2 = len(nums) - 1, None, None
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        n1 = i - 1
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[n1]:
            i -= 1 
        n2 = i 
        if n1 == n2:
            return None
        nums[n1], nums[n2] = nums[n2], nums[n1]
        for tail in range(n1,len(nums)):
            i = len(nums)-1
            while i > tail+1:
                if nums[i] < nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
✔ Accepted
  ✔ 265/265 cases passed (48 ms)
  ✔ Your runtime beats 81.38 % of python3 submissions
  ✔ Your memory usage beats 5.56 % of python3 submissions (13.8 MB)
