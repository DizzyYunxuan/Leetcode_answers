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
            cur = stack[-1]
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
            if not cur.left and not cur.right:
                res.append(cur.val)





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
