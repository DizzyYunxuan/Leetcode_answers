#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        start, mid = self.splitnodes(head)
        mid = self.reverse(mid)
        newhead = self.mergenodes(start, mid)
        return newhead

    def splitnodes(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid

    def reverse(self, head):
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
    
    def mergenodes(self, h1, h2):
        dummy = newhead = ListNode(0)
        while h1 and h2:
            dummy.next = h1
            h1 = h1.next
            dummy.next.next = h2
            h2 = h2.next
            dummy = dummy.next.next
        if h1:
            dummy.next = h1
        elif h2:
            dummy.next = h2
        return newhead.next
✔ Accepted
  ✔ 13/13 cases passed (92 ms)
  ✔ Your runtime beats 89.39 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (22.2 MB)

#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head:
#             return
#         s1, worker = [], head
#         while worker:
#             s1.append(worker)
#             worker = worker.next
#         length = len(s1)     
#         s2 = s1[length//2:]
#         s1 = s1[:length//2]
#         if s1:
#             worker = s1.pop(0)
#         else:
#             return
#         while s1 and s2:
#             worker.next = s2.pop()
#             worker = worker.next
#             worker.next = s1.pop(0)
#             worker = worker.next
#         while s2:
#             worker.next = s2.pop()
#             worker = worker.next
#         worker.next = None


# ✔ Accepted
#   ✔ 13/13 cases passed (124 ms)
#   ✔ Your runtime beats 8.37 % of python3 submissions
#   ✔ Your memory usage beats 15.38 % of python3 submissions (22 MB)
# if __name__ == "__main__":
#     head = worker = ListNode(1)
#     for i in range(2, 6):
#         worker.next = ListNode(i)
#         worker = worker.next

#     Solution().reorderList(head)
