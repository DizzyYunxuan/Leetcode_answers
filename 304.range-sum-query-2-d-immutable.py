#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.matrix[i][j] = \
                self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1] + matrix[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s1 = self.matrix[row1][col1]
        s2 = self.matrix[row1][col2+1]
        s3 = self.matrix[row2+1][col1]
        s = self.matrix[row2+1][col2+1]
        return s-s2-s3+s1

Accepted
12/12 cases passed (132 ms)
Your runtime beats 50.45 % of python3 submissions
Your memory usage beats 16.67 % of python3 submissions (16.6 MB)
# if __name__ == "__main__":
#     matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

#     obj = NumMatrix([[]])
#     param_1 = obj.sumRegion(1,2,2,4)   
#     print(param_1)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# @lc code=end




