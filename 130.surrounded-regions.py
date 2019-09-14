#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        for j in [0, len(board[0])-1]:
            for i in range(len(board)):
                if board[i][j] == 'O':
                    self.dfs(i, j, board)
        
        for j in [0, len(board)-1]:
            for i in range(len(board[0])):
                if board[j][i] == 'O':
                    self.dfs(j, i, board) 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        
        
    def dfs(self, i, j, board):
        board[i][j] = 'A'
        direction = [[i+1,j], [i-1,j],[i,j+1],[i,j-1]]
        for x, y in direction:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                self.dfs(x,y,board)           
   ✔ Accepted
  ✔ 59/59 cases passed (152 ms)
  ✔ Your runtime beats 94.67 % of python3 submissions
  ✔ Your memory usage beats 13.33 % of python3 submissions (15.4 MB)             


# if __name__ == "__main__":
#     board = [
#         ['X','X','X','X'],
#         ['X','O','O','X'],
#         ['X','X','O','X'],
#         ['X','O','X','X'],
#     ]

#     # board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
#     Solution().solve(board)
