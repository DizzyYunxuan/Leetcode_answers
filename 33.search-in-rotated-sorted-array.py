#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        if target >= nums[0]:
            i = 0
            while i < len(nums):
                if nums[i] == target:
                    return i
                elif nums[i] > target:
                    return -1
                i += 1
        else:
            i = len(nums)-1
            while i > 0:
                if nums[i] == target:
                    return i
                elif nums[i] < target:
                    return -1
                i -= 1
        return -1
✔ Accepted
  ✔ 196/196 cases passed (40 ms)
  ✔ Your runtime beats 99.01 % of python3 submissions
  ✔ Your memory usage beats 6.29 % of python3 submissions (14.1 MB)
# class Solution:
#     def search(self, nums, target: int) -> int:
#         try:
#             res = nums.index(target)
#             return res
#         except ValueError:
#             return -1
# ✔ Accepted
#   ✔ 196/196 cases passed (52 ms)
#   ✔ Your runtime beats 46.11 % of python3 submissions
#   ✔ Your memory usage beats 6.29 % of python3 submissions (14 MB)

# if __name__ == '__main__':
#     res = Solution().search([1], 0)
#     print(res)
