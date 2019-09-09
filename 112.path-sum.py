#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:
            return True
        else:
            left = self.hasPathSum(root.left, sum-root.val)
            right = self.hasPathSum(root.right, sum-root.val)
            return left or right

✔ Accepted
  ✔ 114/114 cases passed (56 ms)
  ✔ Your runtime beats 28.02 % of python3 submissions
  ✔ Your memory usage beats 5.45 % of python3 submissions (15.5 MB)

