#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        worker, stack, res = root, [], []
        while worker or stack:
            while worker:
                stack.append(worker)
                worker = worker.left
            worker = stack.pop()
            res.append(worker.val)
            worker = worker.right
        return res
✔ Accepted
  ✔ 68/68 cases passed (36 ms)
  ✔ Your runtime beats 72.03 % of python3 submissions
  ✔ Your memory usage beats 6.56 % of python3 submissions (13.9 MB)


    def inorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        self.inorder(root, path)
        return path

    def inorder(self, root, path):
        if not root:
            return
        self.inorder(root.left, path)
        path += [root.val]
        self.inorder(root.right, path)
    ✔ Accepted
  ✔ 68/68 cases passed (32 ms)
  ✔ Your runtime beats 92.8 % of python3 submissions
  ✔ Your memory usage beats 6.56 % of python3 submissions (13.7 MB)

# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.right = TreeNode(2)
#     root.right.left = TreeNode(3)
#     res = Solution().inorderTraversal(root)
