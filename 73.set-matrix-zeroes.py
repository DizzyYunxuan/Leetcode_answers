#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows, col = [], []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    col.append(j)
        rows, col = set(rows), set(col)
        for i in rows:
            matrix[i][:] = map(lambda x: 0, matrix[i][:])
        for j in col:
            for k in range(m):
                matrix[k][j] =  0
✔ Accepted
  ✔ 159/159 cases passed (152 ms)
  ✔ Your runtime beats 78.14 % of python3 submissions
  ✔ Your memory usage beats 5.13 % of python3 submissions (14.6 MB)
# if __name__ == "__main__":
#     matrix = [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]

#     res = Solution().setZeroes(matrix)
