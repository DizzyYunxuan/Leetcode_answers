#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.gra, self.visited = [[] for _ in range(numCourses)], [0 for _ in range(numCourses)]
        for cur, nx in prerequisites:
            self.gra[cur].append(nx)

        for start in range(numCourses):
            if not self.dfs(start):
                return False
        return True

    def dfs(self, cur):
        if self.visited[cur] == -1:
            return False
        elif self.visited[cur] == 1:
            return True
        self.visited[cur] = -1
        for nx in self.gra[cur]:
            if not self.dfs(nx):
                return False
        self.visited[cur] = 1
        return True
✔ Accepted
  ✔ 42/42 cases passed (120 ms)
  ✔ Your runtime beats 42.02 % of python3 submissions
  ✔ Your memory usage beats 18.37 % of python3 submissions (16.4 MB)
