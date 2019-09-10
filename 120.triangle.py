#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
class Solution:
    def minimumTotal(self, triangle) -> int:
        if not triangle:
            return 0
        res = triangle[-1]
        for i in range(-2, -len(triangle)-1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]

✔ Accepted
  ✔ 43/43 cases passed (60 ms)
  ✔ Your runtime beats 99.22 % of python3 submissions
  ✔ Your memory usage beats 6.67 % of python3 submissions (14.7 MB)
# if __name__ == "__main__":
#     matrix = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#     res = Solution().minimumTotal(matrix)
