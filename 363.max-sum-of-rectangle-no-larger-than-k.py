#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix, k: int) -> int:
        import bisect
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(col):
            row_s = [0] * row
            for right in range(left, col):
                for i in range(row):
                    row_s[i] += matrix[i][right]
                l, cr = [0], 0
                for t in row_s:
                    cr += t
                    loc = bisect.bisect_left(l, cr - k)
                    if loc < len(l):
                        res = max(res, cr-l[loc])
                    bisect.insort(l, cr)
        return res


# if __name__ == "__main__":
#     matrix = [[1,0,1],[0,-2,3]]
#     # matrix = [[2,2,-1]]
#     k = 2
#     res = Solution().maxSumSubmatrix(matrix, k)
#     print(res)
# @lc code=end

