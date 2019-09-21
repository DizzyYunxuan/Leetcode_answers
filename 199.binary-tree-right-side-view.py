#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, self.d = [], {}
        self.leveltravel(root, 1)
        for node in self.d.values():
            res.append(node[-1])
        return res

    def leveltravel(self, root, depth):
        if not root:
            return
        if not depth in self.d:
            self.d[depth] = [root.val]
        else:
            self.d[depth].append(root.val)
        self.leveltravel(root.left, depth+1)
        self.leveltravel(root.right, depth+1)
✔ Accepted
  ✔ 211/211 cases passed (32 ms)
  ✔ Your runtime beats 96.83 % of python3 submissions
  ✔ Your memory usage beats 5.26 % of python3 submissions (13.8 MB)
    

