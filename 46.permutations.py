#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums):
        res = []
        self.getAllp(nums, [], res)
        return res
    def getAllp(self, nums, path, res):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.getAllp(nums[:i]+nums[i+1:], path+[nums[i]], res)
✔ Accepted
  ✔ 25/25 cases passed (48 ms)
  ✔ Your runtime beats 71.1 % of python3 submissions
  ✔ Your memory usage beats 5.36 % of python3 submissions (13.6 MB)
# if __name__ == "__main__":
#     res = Solution().permute([1,2,3])
