#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
class Solution:
    def search(self, nums, target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return True
            while left < mid and nums[left] == nums[mid]:
                left += 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
# ✔ Accepted
#   ✔ 275/275 cases passed (56 ms)
#   ✔ Your runtime beats 97.19 % of python3 submissions
#   ✔ Your memory usage beats 5.72 % of python3 submissions (14.4 MB)
