#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.sovler(root, [], sum, res)
        return res

    def sovler(self, root, path, sum, res):
        if not root:
            return
        elif not root.left and not root.right and root.val == sum:
            res.append(path+[root.val])
            return
        else:
            self.sovler(root.left, path+[root.val], sum-root.val, res)
            self.sovler(root.right, path+[root.val], sum-root.val, res)
✔ Accepted
  ✔ 114/114 cases passed (56 ms)
  ✔ Your runtime beats 61.58 % of python3 submissions
  ✔ Your memory usage beats 6.9 % of python3 submissions (18.9 MB)

