#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path = []
        self.search(root, p, q, [])
        # print(len(self.path))
        p1, p2 = self.path
        # print(p1[-1], p2[-1])
        # print(len(p1), len(p2))
        i, j = 0, 0
        while i < len(p1) and j < len(p2):
            if p1[i] != p2[i]:
                return p1[i-1]
            i += 1
            j += 1
        return p1[-1]
        
    def search(self, root, p, q, path):
        if not root:
            return
        if root == p or root == q:
            self.path.append(path+[root])
        self.search(root.left, p, q, path + [root])
        self.search(root.right, p, q, path + [root])
        return 
✔ Accepted
  ✔ 31/31 cases passed (2148 ms)
  ✔ Your runtime beats 5 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (417.4 MB)
