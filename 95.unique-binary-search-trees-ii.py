#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int): #-> list[TreeNode]:
        if n:
            return self.solver(1, n)
        else:
            return []
    def solver(self, start, end):
        if start > end:
            return [None]
        all_tree = []
        for i in range(start, end+1):
            left = self.solver(start, i-1)
            right = self.solver(i+1, end)

            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    all_tree.append(node)     
        return all_tree
✔ Accepted
  ✔ 9/9 cases passed (56 ms)
  ✔ Your runtime beats 84.22 % of python3 submissions
  ✔ Your memory usage beats 6.67 % of python3 submissions (15.5 MB)

            
# if __name__ == "__main__":
#     res = Solution().generateTrees(3)
#     print(res)

