#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0
✔ Accepted
  ✔ 39/39 cases passed (48 ms)
  ✔ Your runtime beats 76.59 % of python3 submissions
  ✔ Your memory usage beats 5.21 % of python3 submissions (16.2 MB)
