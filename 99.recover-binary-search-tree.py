#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.pre = None, None, TreeNode(float('-inf'))
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def inorder(self, root):
        if not root:
            return       
        self.inorder(root.left)
        if not self.first and self.pre.val >= root.val:
            self.first = self.pre
        if self.first and self.pre.val >= root.val:
            self.second = root
        self.pre = root
        self.inorder(root.right)    
✔ Accepted
  ✔ 1917/1917 cases passed (76 ms)
  ✔ Your runtime beats 64.99 % of python3 submissions
  ✔ Your memory usage beats 25 % of python3 submissions (14.1 MB)

