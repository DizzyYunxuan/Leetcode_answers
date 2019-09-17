#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            if cur:
                res.insert(0, cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        return res
#  ✔ Accepted
#   ✔ 68/68 cases passed (40 ms)
#   ✔ Your runtime beats 39.9 % of python3 submissions
#   ✔ Your memory usage beats 5.72 % of python3 submissions (13.9 MB)           





#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.solver(root)
#         return self.res

#     def solver(self, root):
#         if not root:
#             return
#         self.solver(root.left)
#         self.solver(root.right)
#         self.res.append(root.val)
# ✔ Accepted
#   ✔ 68/68 cases passed (40 ms)
#   ✔ Your runtime beats 39.9 % of python3 submissions
#   ✔ Your memory usage beats 5.72 % of python3 submissions (14 MB)
