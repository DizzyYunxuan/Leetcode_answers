#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # topo sort
        stack = dict.fromkeys(range(numCourses), [])
        for cur, pre in prerequisites:
            stack[cur] = stack.get(cur, []) + [pre]
        toposort = []
        while stack:
            flag = False
            for idx in stack:
                if not stack[idx]:
                    flag = True
                    break
            if not flag:
                return []
            toposort.append(idx)
            stack.pop(idx)
            for pres in stack:
                if idx in stack[pres]:
                    stack[pres].remove(idx)
        return toposort
✔ Accepted
  ✔ 44/44 cases passed (380 ms)
  ✔ Your runtime beats 6.38 % of python3 submissions
  ✔ Your memory usage beats 78.57 % of python3 submissions (14.8 MB)

# if __name__ == "__main__":
#     rs = Solution().findOrder(2, [[0,1],[1,0]])

