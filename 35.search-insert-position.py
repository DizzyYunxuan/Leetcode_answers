#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     try:
    #         return nums.index(target)
    #     except ValueError:
    #         low, high = 0, len(nums) - 1
    #         while low <= high:
    #             mid = (low + high) // 2
    #             if nums[mid] == target:
    #                 return mid
    #             if nums[mid] < target:
    #                 low = mid + 1
    #             elif nums[mid] > target:
    #                 high = mid - 1
    #         return low

# ✔ Accepted
#   ✔ 62/62 cases passed (60 ms)
#   ✔ Your runtime beats 60.96 % of python3 submissions
#   ✔ Your memory usage beats 5.97 % of python3 submissions (14.3 MB)
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return low
# ✔ Accepted
#   ✔ 62/62 cases passed (56 ms)
#   ✔ Your runtime beats 86.85 % of python3 submissions
#   ✔ Your memory usage beats 5.97 % of python3 submissions (14.4 MB)
