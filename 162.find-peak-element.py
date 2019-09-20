#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high-1:
            mid = (low + high) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid - 1
        return low if nums[low] >= nums[high] else high
✔ Accepted
  ✔ 59/59 cases passed (52 ms)
  ✔ Your runtime beats 84.11 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (14.1 MB)

