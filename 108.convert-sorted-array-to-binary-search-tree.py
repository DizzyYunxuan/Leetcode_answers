#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root
✔ Accepted
  ✔ 32/32 cases passed (80 ms)
  ✔ Your runtime beats 55.09 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (16.2 MB)
    

