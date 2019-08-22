#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2, f = l1, l2, ListNode(0)
        end = f
        while n1 and n2:
            if n1.val <= n2.val:
                end.next = n1
                n1 = n1.next
                end = end.next
            else:
                end.next = n2
                n2 = n2.next
                end = end.next
        end.next = n1 or n2
        return f.next
# ✔ Accepted
#   ✔ 208/208 cases passed (36 ms)
#   ✔ Your runtime beats 96.72 % of python3 submissions
#   ✔ Your memory usage beats 5.08 % of python3 submissions (13.7 MB)
    
