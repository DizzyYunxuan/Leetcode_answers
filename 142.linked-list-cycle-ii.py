#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        try:
            slow, fast = head, head.next
            while fast != slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return
        
        slow = slow.next
        while head != slow:
            slow = slow.next
            head = head.next
        return head
            
#     def detectCycle(self, head: ListNode) -> ListNode:
#         worker, dc = head, []
#         while worker:
#             if worker in dc:
#                 return worker
#             dc.append(worker)
#             worker = worker.next
#         return 
# ✔ Accepted
#   ✔ 16/16 cases passed (1240 ms)
#   ✔ Your runtime beats 5.16 % of python3 submissions
#   ✔ Your memory usage beats 100 % of python3 submissions (16.8 MB)

