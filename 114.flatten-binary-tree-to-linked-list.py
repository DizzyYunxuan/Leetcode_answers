#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
✔ Accepted
  ✔ 225/225 cases passed (36 ms)
  ✔ Your runtime beats 97.01 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (14 MB)
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = self.flatten(root.left)
        self.flatten(root.right)
        worker, oriright = left, root.right
        if left:
            root.right = left
        if worker:
            while worker.right:
                worker = worker.right
            worker.right = oriright
        root.left = None
        return root 
✔ Accepted
  ✔ 225/225 cases passed (44 ms)
  ✔ Your runtime beats 59.39 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (14 MB)
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left, root.right = TreeNode(2), TreeNode(5)
#     root.left.left, root.left.right = TreeNode(3), TreeNode(4)
#     root.right.right = TreeNode(6)

#     res = Solution().flatten(root)

