#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = pre = ListNode(0) 
        pre.next = cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
                continue
            pre = cur
            cur = cur.next
        return dummy.next
✔ Accepted
  ✔ 65/65 cases passed (76 ms)
  ✔ Your runtime beats 66.99 % of python3 submissions
  ✔ Your memory usage beats 5.55 % of python3 submissions (16.7 MB)
