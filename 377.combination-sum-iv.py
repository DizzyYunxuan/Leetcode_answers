#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.res, self.memo = 0, {}
        self.solver(nums, target, 0)
        return self.res
    
    def solver(self, nums, target, cur):
        if cur > target: 
            return
        elif cur == target:
            self.res += 1
            return
        for i in nums:
            self.solver(nums, target, cur+i)



# @lc code=end

