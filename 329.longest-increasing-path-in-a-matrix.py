#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

Accepted
138/138 cases passed (392 ms)
Your runtime beats 95.02 % of python3 submissions
Your memory usage beats 53.85 % of python3 submissions (14.3 MB)



#     def longestIncreasingPath(self, matrix) -> int:
#         if not matrix: return 0
#         self.longest, self.memo = 0, {}
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 self.dfs(matrix, 1, i, j, float('-inf'))
#         return self.longest

#     def dfs(self, matrix, longest, x, y, pre):
#         if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
#             return 0
#         if matrix[x][y] == '-':
#             return 0

#         if matrix[x][y] > pre:
#             if (x, y) in self.memo:
#                 self.longest = max(self.longest, longest+self.memo[(x, y)])
#                 return self.memo[(x, y)]
#             else:
#                 self.memo[(x,y)] = 1

#             m = matrix[x][y]
#             matrix[x][y] = '-'
#             directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
#             for d in directions:
#                 curl = longest + self.dfs(matrix, longest, d[0], d[1], m)
#                 self.memo[(x, y)] = max(self.memo[(x, y)], curl)
#             matrix[x][y] = m
#             self.longest = max(self.memo[(x, y)], self.longest)
#             return self.memo[(x, y)]
#         else:
#             return 0
# Accepted
# 138/138 cases passed (1012 ms)
# Your runtime beats 5.04 % of python3 submissions
# Your memory usage beats 30.77 % of python3 submissions (15.5 MB)
# if __name__ == "__main__":
#     matrix = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
#     res = Solution().longestIncreasingPath(matrix)
        
# @lc code=end

