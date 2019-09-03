#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                i = 0
                while i < len(matrix[0]):
                    if matrix[mid][i] > target:
                        return False
                    elif matrix[mid][i] ==  target:
                        return True
                    i += 1
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
        return False
✔ Accepted
  ✔ 136/136 cases passed (72 ms)
  ✔ Your runtime beats 94.99 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (15.8 MB)  
# if __name__ == "__main__":
#     matrix = matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
    # matrix = [[1]]
    # res = Solution().searchMatrix(matrix, 2)
    # print(res)
