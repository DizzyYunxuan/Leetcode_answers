#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def swapPairs(self, head):
#         if not head:
#             return None
#         l = []
#         cur = head
#         while cur:
#             t = cur
#             cur = cur.next
#             t.next = None
#             l.append(t)
#         for i in range(0, len(l), 2):
#             if i+1 < len(l):
#                 l[i], l[i+1] = l[i+1], l[i]
#         head = l[0]
#         for i in range(len(l)-1):
#             l[i].next = l[i+1]
#         return head
# ✔ Accepted
#   ✔ 55/55 cases passed (36 ms)
#   ✔ Your runtime beats 78.44 % of python3 submissions
#   ✔ Your memory usage beats 6.06 % of python3 submissions (13.9 MB)

class Solution:
    def swapPairs(self, head):
        cur = head
        pre = ListNode(None)
        pre.next = cur
        head = pre
        while cur and cur.next:
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = cur

            pre = pre.next.next
            cur = pre.next
        return head.next
✔ Accepted
  ✔ 55/55 cases passed (36 ms)
  ✔ Your runtime beats 78.44 % of python3 submissions
  ✔ Your memory usage beats 6.06 % of python3 submissions (13.9 MB)
# if __name__ == '__main__':
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     res = Solution().swapPairs(head)
#     print(res)

