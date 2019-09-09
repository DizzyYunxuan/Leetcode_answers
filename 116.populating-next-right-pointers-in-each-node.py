#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ori = root
        while root and root.left:
            nextlevel = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = nextlevel
        return ori
✔ Accepted
  ✔ 12/12 cases passed (52 ms)
  ✔ Your runtime beats 99.95 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (16 MB)


    def connect(self, root: 'Node') -> 'Node':
        self.depth = {}
        self.solver(root, 0)
        for depth in self.depth:
            for cn in range(len(self.depth[depth])-1):
                self.depth[depth][cn].next = self.depth[depth][cn+1]
        return root
        
    def solver(self, root, depth):
        if not root:
            return 
        if depth in self.depth:
            self.depth[depth].append(root)
        else:
            self.depth[depth] = [root]
        self.solver(root.left, depth+1)
        self.solver(root.right, depth+1)

✔ Accepted
  ✔ 12/12 cases passed (72 ms)
  ✔ Your runtime beats 44.59 % of python3 submissions
  ✔ Your memory usage beats 7.14 % of python3 submissions (16 MB)
