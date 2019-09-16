#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        cur, pos = head, head.next
        while cur.next:
            cur.next = dummy
            dummy = cur
            cur = pos
            pos = pos.next
        cur.next = dummy
        head.next = None
        return cur
✔ Accepted
  ✔ 27/27 cases passed (40 ms)
  ✔ Your runtime beats 83.45 % of python3 submissions
  ✔ Your memory usage beats 31.82 % of python3 submissions (14.7 MB)         
