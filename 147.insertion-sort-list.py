#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = p = ListNode(0)
        cur = p.next = head
        while cur and cur.next:
            val = cur.val
            if val < cur.next.val:
                cur = cur.next
                continue
            if p.next.val > cur.next.val:
                p = dummy
            while p.next.val < cur.next.val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next
   ✔ Accepted
  ✔ 22/22 cases passed (176 ms)
  ✔ Your runtime beats 84.1 % of python3 submissions
  ✔ Your memory usage beats 25 % of python3 submissions (15.7 MB)         


#     def insertionSortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         dummy = ListNode(float('-inf'))
#         worker = dummy 
#         cur, p = head, head.next
#         while cur:
#             while worker.next and worker.next.val < cur.val:
#                 worker = worker.next
#             cur.next = worker.next
#             worker.next = cur           
#             worker, cur = dummy, p
#             if p:
#                 p = p.next
#         return dummy.next
# ✔ Accepted
#   ✔ 22/22 cases passed (1952 ms)
#   ✔ Your runtime beats 26.21 % of python3 submissions
#   ✔ Your memory usage beats 25 % of python3 submissions (15.4 MB)

# if __name__ == "__main__":
#     head = ListNode(4)
#     head.next = ListNode(2)
#     head.next.next = ListNode(1)
#     head.next.next.next = ListNode(3)
#     res = Solution().insertionSortList(head)
