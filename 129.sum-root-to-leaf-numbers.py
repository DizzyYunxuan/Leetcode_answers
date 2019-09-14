#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.sovler(root, 0)
        return self.sum
    
    def sovler(self, root, path):
        if not root:
            return
        path = path * 10 + root.val
        if not root.left and not root.right:
            self.sum += path
            return
        self.sovler(root.left, path)
        self.sovler(root.right, path)
# ✔ Accepted
#   ✔ 110/110 cases passed (28 ms)
#   ✔ Your runtime beats 99.68 % of python3 submissions
#   ✔ Your memory usage beats 5.55 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)


    # res = Solution().sumNumbers(root)
