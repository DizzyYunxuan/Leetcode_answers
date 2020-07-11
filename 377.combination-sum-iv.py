#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.solver(nums, target)
    
    def solver(self, nums, target):
        if target in self.memo:
            return self.memo[target]
        else:
            res = 0
            for i in nums:
                if i <= target:
                    nt = target - i
                    if nt == 0:
                        res += 1
                        continue
                    res += self.solver(nums, nt)
            self.memo[target] = res
        return res
        
Accepted
17/17 cases passed (40 ms)
Your runtime beats 90.53 % of python3 submissions
Your memory usage beats 22.22 % of python3 submissions (15.8 MB)


# @lc code=end

