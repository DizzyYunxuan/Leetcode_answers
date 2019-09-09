#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p or not q):
            return False
        elif p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right
✔ Accepted
  ✔ 57/57 cases passed (28 ms)
  ✔ Your runtime beats 98.82 % of python3 submissions
  ✔ Your memory usage beats 5.72 % of python3 submissions (13.8 MB)
