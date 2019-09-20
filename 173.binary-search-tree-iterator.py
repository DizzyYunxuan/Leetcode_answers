#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.vals = []
        self.visited = 0
        self.root = root
        self.nextval = 0
        self.midorder(root)
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.visited += 1
        return self.vals[self.visited-1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.visited >= len(self.vals):
            return False
        else:
            return True
    def midorder(self, root):
        if not root:
            return
        self.midorder(root.left)
        self.vals.append(root.val)
        self.midorder(root.right)
✔ Accepted
  ✔ 62/62 cases passed (104 ms)
  ✔ Your runtime beats 11.84 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (21.3 MB)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

