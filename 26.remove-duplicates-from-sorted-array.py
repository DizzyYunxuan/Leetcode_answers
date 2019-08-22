#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         res = list(set(nums))
#         res.sort()
#         for i in range(len(res)):
#             nums.insert(i, res[i])
#         return len(res)
# ✔ Accepted
#   ✔ 161/161 cases passed (176 ms)
#   ✔ Your runtime beats 8.54 % of python3 submissions
#   ✔ Your memory usage beats 5.74 % of python3 submissions (15.5 MB)

# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         if not nums:
#             return 0
#         i, cur = 1, nums[0]
#         length = len(nums)
#         while i < length:
#             if nums[i] == cur:
#                 del nums[i]
#             else:
#                 cur = nums[i]
#                 i += 1
#             length = len(nums)
#         return len(nums)
# ✔ Accepted
#   ✔ 161/161 cases passed (116 ms)
#   ✔ Your runtime beats 22.91 % of python3 submissions
#   ✔ Your memory usage beats 5.74 % of python3 submissions (15.4 MB)
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums: 
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
✔ Accepted
  ✔ 161/161 cases passed (88 ms)
  ✔ Your runtime beats 97.89 % of python3 submissions
  ✔ Your memory usage beats 5.74 % of python3 submissions (15.3 MB)
# if __name__ == '__main__':
#     res = Solution().removeDuplicates([1,1,2])
#     print(res)

