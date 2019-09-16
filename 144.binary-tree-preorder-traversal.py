#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return
        stack, res, worker = [root], [], root
        while stack:
            while worker:
                res.append(worker.val)
                stack.append(worker)
                worker = worker.left
            worker = stack.pop()
            worker = worker.right
            stack.append(worker)
        return res



if __name__ == "__main__":
    root  = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    res = Solution().preorderTraversal(root)

#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         self.res = []
#         self.solver(root)
#         return self.res

#     def solver(self, root):
#         if not root:
#             return
#         self.res.append(root.val)
#         self.solver(root.left)
#         self.solver(root.right)
# ✔ Accepted
#   ✔ 68/68 cases passed (36 ms)
#   ✔ Your runtime beats 73.11 % of python3 submissions
#   ✔ Your memory usage beats 6.52 % of python3 submissions (13.6 MB)
