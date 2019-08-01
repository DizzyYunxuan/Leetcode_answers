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


# if __name__ == '__main__':
#     res = Solution().maxArea([2,3,4,5,18,17,6])
#     print(res)
