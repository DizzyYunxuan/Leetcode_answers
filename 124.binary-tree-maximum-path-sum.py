#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ms = float('-inf')
        self.solver(root)
        return self.ms
    
    def solver(self, root):
        if not root:
            return 0
        left = max(self.solver(root.left), 0)
        right = max(self.solver(root.right), 0)
        self.ms = max(self.ms, root.val + left + right)
        return max(root.val + left, root.val + right)
✔ Accepted
  ✔ 93/93 cases passed (100 ms)
  ✔ Your runtime beats 70.8 % of python3 submissions
  ✔ Your memory usage beats 38.89 % of python3 submissions (21.3 MB)

# if __name__ == "__main__":
#     root = TreeNode(10)
#     root.left = TreeNode(9)
#     root.right = TreeNode(20)
#     root.right.left = TreeNode(15)
#     root.right.right = TreeNode(7)
#     res = Solution().maxPathSum(root)
