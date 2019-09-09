#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left or not root.right:
            return self.minDepth(root.left)+self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# ✔ Accepted
#   ✔ 41/41 cases passed (56 ms)
#   ✔ Your runtime beats 38.6 % of python3 submissions
#   ✔ Your memory usage beats 8.11 % of python3 submissions (16.2 MB)  

