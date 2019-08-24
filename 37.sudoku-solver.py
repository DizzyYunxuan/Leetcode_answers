#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Check every '.' in 3 rules, take the intersection
        rowsC, colsC, subboxC, can_dict, wdots = [], [], [], {}, []
        for i in range(len(board)):
            row = board[i]
            col = [r[i] for r in board]
            subbox2d = [j[(i%3)*3:(i%3)*3+3] for j in board[(i//3)*3:(i//3)*3+3]]
            subbox1d = []
            for j in subbox2d:
                subbox1d += j
            rowsC.append(self.rowsCandidates(row))
            colsC.append(self.colCandidates(col))
            subboxC.append(self.subboxCandidates(subbox1d))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    res = set(rowsC[i]).intersection(set(colsC[j]), set(subboxC[i//3*3+j//3]))
                    can_dict[(i,j)] = res
                    wdots.append((i, j))
        self.dfs(board, wdots, can_dict)

    def rowsCandidates(self, row):
        rowsCan = [str(i+1) for i in range(len(row))]
        for i in row:
            if i != '.':
                rowsCan.remove(i)
        return rowsCan

    def colCandidates(self, column):
        colscan = [str(i+1) for i in range(len(column))]
        for i in column:
            if i != '.':
                colscan.remove(i)
        return colscan
    
    def subboxCandidates(self, subbox):
        subboxCan = [str(i+1) for i in range(len(subbox))]
        for i in subbox:
            if i != '.':
                subboxCan.remove(i)
        return subboxCan

    def dfs(self, board, wdots, can_dict):
        for i in can_dict[wdots[0]]:         
            if self.isOK(board, wdots[0], i): 
                board[wdots[0][0]][wdots[0][1]] = i
                if len(wdots) == 1:
                    return True
                if self.dfs(board, wdots[1:], can_dict):
                    return True
                else:
                    board[wdots[0][0]][wdots[0][1]] = '.'           
        return False     
        
    def isOK(self, board, pos, val):
        for k in range(9):
            if board[pos[0]][k] == val:
                return False
            if board[k][pos[1]] == val:
                return False
            if board[pos[0]//3*3+k//3][pos[1]//3*3+k%3] == val:
                return False
        return True

✔ Accepted
  ✔ 6/6 cases passed (196 ms)
  ✔ Your runtime beats 71.08 % of python3 submissions
  ✔ Your memory usage beats 10.71 % of python3 submissions (14 MB)
# if __name__ == '__main__':
#     board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
#     # board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
#     res = Solution().solveSudoku(board)
#     print(res)
