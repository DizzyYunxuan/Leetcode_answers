#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.dfs(root, '')
        return self.res
    

    def dfs(self, root, path):
        if not root:
            return
        if not root.left and not root.right:
            self.res.append(path+str(root.val))
            return
        self.dfs(root.left, path+str(root.val)+'->')
        self.dfs(root.right, path+str(root.val)+'->')
✔ Accepted
  ✔ 209/209 cases passed (36 ms)
  ✔ Your runtime beats 87.49 % of python3 submissions
  ✔ Your memory usage beats 9.52 % of python3 submissions (13.8 MB)
