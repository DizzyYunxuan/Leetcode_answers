#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.res = {}
        self.solver(root, 0)
        return list(self.res.values())[::-1]

    def solver(self, root, depth):
        if not root:
            return
        if depth in self.res:
            self.res[depth].append(root.val)
        else:
            self.res[depth] = [root.val]
        self.solver(root.left, depth+1)
        self.solver(root.right, depth+1)
✔ Accepted
  ✔ 34/34 cases passed (40 ms)
  ✔ Your runtime beats 81.83 % of python3 submissions
  ✔ Your memory usage beats 7.41 % of python3 submissions (14.2 MB)
