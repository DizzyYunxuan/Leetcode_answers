#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = {}
        self.solver(root, 0)
        l = list(self.res.values())
        for i in range(len(l)):
            if i % 2 != 0:
                l[i] = l[i][::-1]
        return l

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
  ✔ 33/33 cases passed (32 ms)
  ✔ Your runtime beats 97.42 % of python3 submissions
  ✔ Your memory usage beats 5.41 % of python3 submissions (13.8 MB)
