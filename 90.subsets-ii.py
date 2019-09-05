#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        for depth in range(len(nums)+1):
            self.solver(nums, [], depth, res)
        return res

    def solver(self, nums, path, depth, res):
        if len(path) == depth:
            res.append(path)
            return
        for i in range(len(nums)):    
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.solver(nums[i+1:], path+[nums[i]], depth, res)

if __name__ == "__main__":
    nums = [1,2,2]
    res = Solution().subsetsWithDup(nums)

