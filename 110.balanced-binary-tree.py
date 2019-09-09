#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = self.solver(root)
        return True if res != 'No' else False
    
    def solver(self, root):
        if not root:
            return 0
        left = self.solver(root.left)
        right = self.solver(root.right)
        if right == 'No' or left == 'No':
            return 'No'
        else:
            if abs(left - right) > 1:
                return 'No'
            else:
                return max(left, right) + 1
✔ Accepted
  ✔ 227/227 cases passed (60 ms)
  ✔ Your runtime beats 70.39 % of python3 submissions
  ✔ Your memory usage beats 54.29 % of python3 submissions (18.5 MB)

