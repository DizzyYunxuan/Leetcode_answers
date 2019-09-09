#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.solver(root)
    
    def solver(self, root, floor=-float('inf'), ceiling=float('inf')):
        if not root:
            return True   
        if root.val <= floor or root.val >= ceiling:
            return False       
        left = self.solver(root.left, floor, root.val)
        right = self.solver(root.right, root.val, ceiling)
        return left and right
✔ Accepted
  ✔ 75/75 cases passed (48 ms)
  ✔ Your runtime beats 91.68 % of python3 submissions
  ✔ Your memory usage beats 10.35 % of python3 submissions (16.4 MB)


#     def isValidBST(self, root: TreeNode) -> bool:
#         res = []
#         self.inorder(root, res)
#         for i in range(1, len(res)):
#             if res[i-1] >= res[i]:
#                 return False
#         return True

#     def inorder(self, root, res):
#         if not root:
#             return
#         self.inorder(root.left, res)
#         res.append(root.val)
#         self.inorder(root.right, res)
# ✔ Accepted
#   ✔ 75/75 cases passed (52 ms)
#   ✔ Your runtime beats 74.82 % of python3 submissions
#   ✔ Your memory usage beats 5.75 % of python3 submissions (16.8 MB)
        
