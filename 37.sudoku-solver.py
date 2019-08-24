#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Check every '.' in 3 rules, take the intersection
        for i in range(len(board)):
            for j in range(len(i)):
                if board[i][j] == '.':
                    rowsSet = rowsCandidates()
                    columsSet = colCandidates()
                    sbbSet = subboxCandidates()
                    board[i][j] = rowsSet.intersection(columsSet, sbbSet)
        
    def rowsCandidates(self, row):

    def colCandidates(self, column):
    def subboxCandidates(self, subbox):


