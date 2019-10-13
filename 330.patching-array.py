#
# @lc app=leetcode id=330 lang=python3
#
# [330] Patching Array
#

# @lc code=start
class Solution:
    def minPatches(self, nums, n: int) -> int:
        miss, i, add = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                add += 1
        return add
Accepted
149/149 cases passed (72 ms)
Your runtime beats 71.68 % of python3 submissions
Your memory usage beats 50 % of python3 submissions (13.9 MB)
        

# if __name__ == "__main__":
#     res = Solution().minPatches([1,5,10], 20)
# @lc code=end

