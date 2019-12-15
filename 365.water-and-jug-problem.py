#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        import math
        if x + y < z: return False
        if x == z or y == z or x + y == z: return True
        return z % math.gcd(x, y) == 0
Accepted
34/34 cases passed (24 ms)
Your runtime beats 94.34 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.7 MB)




#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         queue, visited = [(0, 0)], {(0, 0): 1}

#         while queue:
#             cx, cy = queue.pop(0)
#             if z in [cx + cy, cx, cy]: return True
#             for state in [(x, cy), (cx, y), 
#                             (0, cy), (cx, 0),
#                             (cx+cy-y, y) if cx+cy >= y else (0, cx+cy) ,
#                             (x, cx+cy-x) if cx+cy >= x else (cx+cy, 0)]:
#                 if state not in visited:
#                     queue.append(state)
#                     visited[state] = 1
#         return False
# # BFS
# Accepted
# 34/34 cases passed (2120 ms)
# Your runtime beats 5.13 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (86.6 MB)

# @lc code=end

