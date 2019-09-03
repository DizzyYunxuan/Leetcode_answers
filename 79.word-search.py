#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.solver([i, j], [[i, j]], board, word, m, n):
                    return True
        return False
                        
    def solver(self, pos, path, board, word, m, n):
        if board[pos[0]][pos[1]] == word[0]:
            if len(word) == 1:
                return True
            up, right, down, left = [pos[0]-1, pos[1]], [pos[0], pos[1]+1], \
                [pos[0]+1, pos[1]], [pos[0], pos[1]-1]
            if up[0] >= 0 and up not in path and self.solver(up, path+[up], board, word[1:], m, n):
                return True
            if right[1] < n and right not in path and self.solver(right, path+[right], board, word[1:],m, n):
                return True
            if down[0] < m and down not in path and self.solver(down, path+[down], board, word[1:], m, n):
                return True
            if left[1] >= 0 and left not in path and self.solver(left, path+[left], board, word[1:], m, n):
                return True
✔ Accepted
  ✔ 87/87 cases passed (396 ms)
  ✔ Your runtime beats 51.57 % of python3 submissions
  ✔ Your memory usage beats 12.76 % of python3 submissions (18.6 MB)           
        
# if __name__ == "__main__":
# #     board =[
# #   ['A','B','C','E'],
# #   ['S','F','C','S'],
# #   ['A','D','E','E']
# # ]
#     board = [['a', 'b']]
#     word = 'ba'
#     # word = 'ABCCED'
#     res = Solution().exist(board, word)
#     print(res)


