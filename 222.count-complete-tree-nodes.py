#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        lheight, rheight, l, r = 0, 0, root, root
        while l:
            l = l.left
            lheight += 1
        while r:
            r = r.right
            rheight += 1
        if lheight == rheight:
            return 2**lheight - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
✔ Accepted
  ✔ 18/18 cases passed (80 ms)
  ✔ Your runtime beats 94.07 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (21.5 MB)


    # def countNodes(self, root: TreeNode) -> int:
#         if not root: return 0
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# ✔ Accepted
#   ✔ 18/18 cases passed (104 ms)
#   ✔ Your runtime beats 32.73 % of python3 submissions
#   ✔ Your memory usage beats 6.9 % of python3 submissions (21.7 MB)
