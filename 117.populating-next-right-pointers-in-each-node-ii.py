#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ori = root
        while root and (root.left or root.right):
            nextroot = root.left or root.right
            curleaf = nextroot 
            while root:
                if root.left and root.right:
                    root.left.next = root.right
                    curleaf = root.right
                elif root.left or root.right:
                    if curleaf != root.left and curleaf != root.right:
                        curleaf.next = root.left or root.right
                        curleaf = curleaf.next
                root = root.next
            root = nextroot
        return ori

                


