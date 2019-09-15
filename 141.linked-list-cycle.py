#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:  
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
    
    
    
    
#     def hasCycle(self, head: ListNode) -> bool:
#         m = []
#         worker = head
#         while worker:
#             if worker in m:
#                 return True
#             m.append(worker)
#             worker = worker.next
#         return False
# ✔ Accepted
#   ✔ 17/17 cases passed (1244 ms)
#   ✔ Your runtime beats 5.41 % of python3 submissions
#   ✔ Your memory usage beats 100 % of python3 submissions (17 MB)
