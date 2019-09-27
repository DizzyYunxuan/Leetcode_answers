#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
✔ Accepted
  ✔ 41/41 cases passed (48 ms)
  ✔ Your runtime beats 43.63 % of python3 submissions
  ✔ Your memory usage beats 9.38 % of python3 submissions (13.9 MB)      

