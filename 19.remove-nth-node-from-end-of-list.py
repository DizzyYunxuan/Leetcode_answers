#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        n_pre, cur = head, head
        if not cur.next:
            return None
        for _ in range(n):
            cur = cur.next
        if cur is None:
            head = head.next
            return head
        else:
            while cur and cur.next:
                cur = cur.next
                n_pre = n_pre.next
            n_pre.next = n_pre.next.next
        return head
# ✔ Accepted
#   ✔ 208/208 cases passed (36 ms)
#   ✔ Your runtime beats 86.69 % of python3 submissions
#   ✔ Your memory usage beats 5.17 % of python3 submissions (13.8 MB)
