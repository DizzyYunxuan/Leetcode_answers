#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
✔ Accepted
  ✔ 68/68 cases passed (36 ms)
  ✔ Your runtime beats 74.02 % of python3 submissions
  ✔ Your memory usage beats 5.41 % of python3 submissions (13.9 MB)
