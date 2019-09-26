#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = 0
        self.solver(root, k)
        return self.res
    
    def solver(self, root, k):
        if not root:
            return
        self.solver(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self.solver(root.right, k)       
✔ Accepted
  ✔ 91/91 cases passed (68 ms)
  ✔ Your runtime beats 27.68 % of python3 submissions
  ✔ Your memory usage beats 5.45 % of python3 submissions (18.1 MB)

