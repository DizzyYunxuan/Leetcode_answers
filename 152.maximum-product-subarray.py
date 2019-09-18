#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
class Solution:
    def maxProduct(self, nums):
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        return max(nums + reverse)
✔ Accepted
  ✔ 184/184 cases passed (68 ms)
  ✔ Your runtime beats 45.22 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (15 MB)              
                    
# if __name__ == "__main__":
#     nums = [2,3,-2,4]
#     res = Solution().maxProduct(nums)

