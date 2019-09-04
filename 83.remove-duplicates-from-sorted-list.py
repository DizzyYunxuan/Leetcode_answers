#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
        cur, pre = head, head
        while cur.next:
            cur = cur.next
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = cur
        return head
✔ Accepted
  ✔ 165/165 cases passed (48 ms)
  ✔ Your runtime beats 69.15 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (13.9 MB)
            


