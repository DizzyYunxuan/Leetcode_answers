#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
class Solution:
    # def firstMissingPositive(self, nums) -> int:
    #     nums.sort()
    #     res = 1
    #     for i in nums:
    #         if i == res:
    #             res += 1
    #     return res            
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            # Build relationship of index and value
            while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

✔ Accepted
  ✔ 165/165 cases passed (40 ms)
  ✔ Your runtime beats 84.34 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (13.8 MB)

