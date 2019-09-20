#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution:
    def findMin(self, nums: List[int]) -> int:   
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid if nums[high] != nums[mid] else high - 1
        return nums[low]
✔ Accepted
  ✔ 192/192 cases passed (64 ms)
  ✔ Your runtime beats 58.96 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (14.3 MB)
