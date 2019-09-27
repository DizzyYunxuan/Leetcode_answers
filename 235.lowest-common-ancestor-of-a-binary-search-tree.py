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
        if not root or not q or not p:
            return 
        
        if max(q.val, p.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(q.val, p.val) > root.val:
            return self.lowestCommonAncestor(root.right,p, q)
        else:
            return root
✔ Accepted
  ✔ 27/27 cases passed (88 ms)
  ✔ Your runtime beats 68.98 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (17.9 MB)
