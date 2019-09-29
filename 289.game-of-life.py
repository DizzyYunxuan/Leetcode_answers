#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changelist = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.ischange(i, j, board):
                    changelist.append([i, j])

        for x, y in changelist:
            board[x][y] = ~board[x][y] + 2
    
    def ischange(self, x, y, board):
        positions = [[x-1, y], [x+1, y], [x, y-1], [x, y+1],\
            [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]
        alives, dies = 0, 0
        for i, j in positions:
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if board[i][j]:
                    alives += 1
                else:
                    dies += 1
        if board[x][y]:
            if alives < 2 or alives > 3:
                return True
        else:
            if alives == 3:
                return True
        return False
✔ Accepted
  ✔ 23/23 cases passed (44 ms)
  ✔ Your runtime beats 27.53 % of python3 submissions
  ✔ Your memory usage beats 10 % of python3 submissions (14 MB)
# if __name__ == "__main__":
#     board = [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
#     Solution().gameOfLife(board)

