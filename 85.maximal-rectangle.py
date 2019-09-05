#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        maxsq = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] = heights[i] + 1
                else:
                    heights[i] = 0
            stack = [-1]
            for i in range(n+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    maxsq = max(maxsq, h * w)
                stack.append(i)
        
        return maxsq

✔ Accepted
  ✔ 66/66 cases passed (212 ms)
  ✔ Your runtime beats 88.97 % of python3 submissions
  ✔ Your memory usage beats 6.25 % of python3 submissions (15 MB)
# if __name__ == "__main__":
#     matrix = [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
#     res = Solution().maximalRectangle(matrix)
