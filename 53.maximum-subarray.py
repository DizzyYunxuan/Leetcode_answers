#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums) -> int:
        m, cm = nums[0], nums[0]
        for i in range(1, len(nums)):
            if cm > 0:
                cm += nums[i]
                m = max(m, cm)
            else:
                cm = nums[i]
                m = max(m, cm)
        return m
✔ Accepted
  ✔ 202/202 cases passed (72 ms)
  ✔ Your runtime beats 92.6 % of python3 submissions
  ✔ Your memory usage beats 5.69 % of python3 submissions (14.5 MB)
# if __name__ == "__main__":
#     res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
