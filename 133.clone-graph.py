#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# Definition for a Node.
# class Node:
#     def __init__(self, val, neighbors):
#         self.val = val
#         self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        newnode = Node(node.val, [])
        queue, visited = [node], {node:newnode}
        while queue:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.append(n)
                visited[cur].neighbors.append(visited[n])
        return newnode
✔ Accepted
  ✔ 20/20 cases passed (40 ms)
  ✔ Your runtime beats 95.05 % of python3 submissions
  ✔ Your memory usage beats 7.41 % of python3 submissions (14.6 MB)
# if __name__ == "__main__":
#     node1 = Node(1,[])
#     node2 = Node(2,[])
#     node3 = Node(3,[])
#     node4 = Node(4,[])
#     node1.neighbors = [node2, node4]
#     node2.neighbors = [node1, node3]
#     node3.neighbors = [node2, node4]
#     node4.neighbors = [node1, node3]
#     Solution().cloneGraph(node1)

