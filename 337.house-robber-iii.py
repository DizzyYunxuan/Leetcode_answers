#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return [root.val + left[1] + right[1], max(left) + max(right)]

Accepted
124/124 cases passed (52 ms)
Your runtime beats 80.24 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (14.9 MB)

# if __name__ == "__main__":
#     root = TreeNode(3)
#     root.left, root.right = TreeNode(4), TreeNode(5)
#     root.left.left = TreeNode(1)
#     root.left.right = TreeNode(3)
#     root.right.right = TreeNode(1)
#     res = Solution().rob(root)
#     print(res)

    # @lc code=end

