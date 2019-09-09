#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        ind = inorder.index(postorder.pop(-1))
        root = TreeNode(inorder[ind])
        root.right = self.buildTree(inorder[ind+1:], postorder)
        root.left = self.buildTree(inorder[:ind], postorder)
        return root
✔ Accepted
  ✔ 203/203 cases passed (132 ms)
  ✔ Your runtime beats 64.62 % of python3 submissions
  ✔ Your memory usage beats 55.56 % of python3 submissions (52.8 MB)
