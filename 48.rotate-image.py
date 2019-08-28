#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

✔ Accepted
  ✔ 21/21 cases passed (36 ms)
  ✔ Your runtime beats 96.24 % of python3 submissions
  ✔ Your memory usage beats 6.25 % of python3 submissions (13.6 MB)

    # def rotate(self, A):
    #     n = len(A)
    #     for i in range(n//2):
    #         for j in range(n-n//2):
    #             A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
    #                      A[~j][i], A[~i][~j], A[j][~i], A[i][j]
# if __name__ == "__main__":
#     a = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
#     Solution().rotate(a)



