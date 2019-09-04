#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        stack, maxsq = [-1], 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                maxsq = max(maxsq, h * w)
            stack.append(i)
        return maxsq
✔ Accepted
  ✔ 96/96 cases passed (124 ms)
  ✔ Your runtime beats 66.3 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (15.4 MB)
# if __name__ == "__main__":
#     res = Solution().largestRectangleArea([2,1,5,6,2,3])
