#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         if not head:
#             return None
#         l = []
#         cur = head
#         while cur:
#             t = cur
#             cur = cur.next
#             t.next = None
#             l.append(t)
#         for i in range(0, len(l), k):
#             if i+k-1 < len(l):
#                 for j in range(k//2):
#                     l[i+j], l[i+k-j-1] = l[i+k-j-1], l[i+j]
#         head = l[0]
#         for i in range(len(l)-1):
#             l[i].next = l[i+1]
#         return head

# ✔ Accepted
#   ✔ 81/81 cases passed (60 ms)
#   ✔ Your runtime beats 28.2 % of python3 submissions
#   ✔ Your memory usage beats 5.88 % of python3 submissions (14.5 MB)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next 
✔ Accepted
  ✔ 81/81 cases passed (52 ms)
  ✔ Your runtime beats 86.93 % of python3 submissions
  ✔ Your memory usage beats 5.88 % of python3 submissions (14.5 MB)

# if __name__ == '__main__':
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     # head.next.next.next.next = ListNode(5)
#     res = Solution().reverseKGroup(head, 2)
#     print(res)

