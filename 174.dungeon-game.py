#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])

        for i in range(cols - 2, -1, -1):
            dp[-1][i] = max(dp[-1][i+1]-dungeon[-1][i], 1)
        
        for i in range(rows - 2, -1, -1):
            dp[i][-1] = max(dp[i+1][-1]-dungeon[i][-1], 1)

        for i in range(len(dungeon)-1)[::-1]:
            for j in range(len(dungeon[0])-1)[::-1]:
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]
✔ Accepted
  ✔ 45/45 cases passed (84 ms)
  ✔ Your runtime beats 72.61 % of python3 submissions
  ✔ Your memory usage beats 11.11 % of python3 submissions (14.8 MB)
  
           
# if __name__ == "__main__":
#     dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
#     # dungeon = [[1,-2,3],[2,-2,-2]]
#     # dungeon = [[2,1],[1,-1]]
#     # dungeon = [[1,-4,5,-99],[2,-2,-2,-1]]
#     # dungeon = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
#     # dungeon = [[-200]]
#     res = Solution().calculateMinimumHP(dungeon)
    

################################ DFS TLE ################################

    # def calculateMinimumHP(self, dungeon) -> int:
    #     self.eachpathlowesthealth = []
    #     self.dfs([0,0], 0, dungeon, 0)
    #     res = max(self.eachpathlowesthealth)
    #     return 1 if res > 0 else -res+1

    # def dfs(self, pos, health, dungeon, lowest_uptonow):
    #     x, y = pos
    #     if x >= len(dungeon) or y >= len(dungeon[0]):
    #         return
    #     health += dungeon[x][y]
    #     lowest_uptonow = min(health, lowest_uptonow)
    #     if x == len(dungeon) - 1 and y == len(dungeon[0]) - 1:
    #         self.eachpathlowesthealth.append(lowest_uptonow)
    #         return       
    #     self.dfs([x+1, y], health, dungeon, lowest_uptonow)
    #     self.dfs([x, y+1], health, dungeon, lowest_uptonow)

################################ DFS TLE ################################




