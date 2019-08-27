#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
class Solution:
    def jump(self, nums) -> int:
        start, end, step, farthest = 0, 1, 0, 0
        while end < len(nums):
            step += 1
            for i in range(start, end):
                if i + nums[i] >= len(nums) - 1:
                    return step
                farthest = max(farthest, i+nums[i])
            start, end = end, farthest+1
        return step
✔ Accepted
  ✔ 92/92 cases passed (112 ms)
  ✔ Your runtime beats 64.03 % of python3 submissions
  ✔ Your memory usage beats 8.33 % of python3 submissions (15.6 MB)           
