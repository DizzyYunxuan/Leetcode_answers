#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = {}
        self.solver(root, 0)
        return list(self.res.values())


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
  ✔ Your runtime beats 80.3 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (14.7 MB)   
    
