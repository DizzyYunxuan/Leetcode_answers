#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
class Solution:
    def subsets(self, nums):
        length,  res = len(nums), []
        for i in range(1, length+1):
            self.solver(nums, i, [], res)
        return res+[[]]
    def solver(self, nums, depth, path, res):
        if depth == len(path):
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                self.solver(nums[i+1:], depth, path+[nums[i]], res)
✔ Accepted
  ✔ 10/10 cases passed (44 ms)
  ✔ Your runtime beats 40.95 % of python3 submissions
  ✔ Your memory usage beats 5.95 % of python3 submissions (14.1 MB)
