#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        self.dfs(root, p, [])
        self.dfs(root, q, [])

    def dfs(self, root, key, path):
        if root == key:
            self.path.append(path)
            return
        if key.val < root.val:
            self.dfs(root.left, key, path + [root])
        else:
            self.dfs(root.right, key, path + [root])

