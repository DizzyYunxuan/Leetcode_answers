#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] <= height[r]:
                l += 1
                if min(height[l], height[r]) * (r - l) > res:
                    res = min(height[l], height[r]) * (r - l)
            else:
                r -= 1
                if min(height[l], height[r]) * (r - l) > res: 
                    res = min(height[l], height[r]) * (r - l)
        return res
# ✔ Accepted
#   ✔ 50/50 cases passed (140 ms)
#   ✔ Your runtime beats 76.38 % of python3 submissions
#   ✔ Your memory usage beats 5.04 % of python3 submissions (15.5 MB)
