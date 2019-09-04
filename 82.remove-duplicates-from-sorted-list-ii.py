#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newhead = pre = ListNode(0)
        newhead.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next
        return newhead.next
✔ Accepted
  ✔ 168/168 cases passed (48 ms)
  ✔ Your runtime beats 69.51 % of python3 submissions
  ✔ Your memory usage beats 8 % of python3 submissions (13.9 MB)
