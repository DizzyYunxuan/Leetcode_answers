#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False
✔ Accepted
  ✔ 129/129 cases passed (56 ms)
  ✔ Your runtime beats 12.66 % of python3 submissions
  ✔ Your memory usage beats 7.41 % of python3 submissions (18.4 MB)
