#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets):
        graph = {}
        for edge in sorted(tickets):
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], [])
        self.res = []
        self.dfs(graph, 'JFK')
        return self.res

    def dfs(self, graph, curnode):
        while graph[curnode]:
            nxt = graph[curnode].pop(0)
            self.dfs(graph, nxt)
        self.res = [curnode] + self.res
Accepted
80/80 cases passed (108 ms)
Your runtime beats 22.89 % of python3 submissions
Your memory usage beats 7.69 % of python3 submissions (14.2 MB)
# if __name__ == "__main__":
#     res = Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
# @lc code=end

