#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    def isValidSudoku(self, board) -> bool:
        cross = 0
        while cross < 9:
            checkr = {}
            checkc = {}
            for i in range(0, 9):
                # Check rows
                if board[cross][i] != '.' and board[cross][i] not in checkr:
                    checkr[board[cross][i]] = 1
                elif board[cross][i] in checkr:
                    return False
                
                # Check columns
                if board[i][cross] != '.' and board[i][cross] not in checkc:
                    checkc[board[i][cross]] = 1
                elif board[i][cross] in checkc:
                    return False
            cross += 1
        
        # Check sub_boxes
        for i in range(9):
            checkbox = {}      
            subbox = [sl[(i%3)*3:(i%3)*3+3] for sl in board[(i//3)*3:(i//3)*3+3]]
            for j in subbox:
                for k in j:
                    if k != '.' and k not in checkbox:
                        checkbox[k] = 1
                    elif k in checkbox:
                        return False
        
        return True
✔ Accepted
  ✔ 504/504 cases passed (104 ms)
  ✔ Your runtime beats 91.28 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (13.8 MB)

