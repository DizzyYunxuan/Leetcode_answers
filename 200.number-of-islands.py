#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.solver(i,j,grid)
                    res += 1
        return res
    def solver(self, x, y, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return    
        if grid[x][y] == '1':
            grid[x][y] = 'I'
        else:
            return
        self.solver(x-1, y, grid)
        self.solver(x+1, y, grid)
        self.solver(x, y-1, grid)
        self.solver(x, y+1, grid)
✔ Accepted
  ✔ 47/47 cases passed (168 ms)
  ✔ Your runtime beats 41.87 % of python3 submissions
  ✔ Your memory usage beats 9.4 % of python3 submissions (14.7 MB)
