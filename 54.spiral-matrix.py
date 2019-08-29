#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:      
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
✔ Accepted
  ✔ 22/22 cases passed (32 ms)
  ✔ Your runtime beats 91.76 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (13.7 MB)
# if __name__ == "__main__":
#     matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#     res = Solution().spiralOrder(matrix)          

