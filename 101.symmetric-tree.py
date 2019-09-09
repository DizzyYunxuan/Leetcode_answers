#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSameTree(root.left, root.right) if root else True
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p or not q):
            return False
        elif p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.right)
        right = self.isSameTree(p.right, q.left)
        return left and right
✔ Accepted
  ✔ 195/195 cases passed (44 ms)
  ✔ Your runtime beats 40.99 % of python3 submissions
  ✔ Your memory usage beats 5.17 % of python3 submissions (14 MB)
