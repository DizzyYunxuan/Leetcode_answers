#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        l, i = [], head
        while i:
            l.append(i.val)
            i = i.next
        m, n = max(m, n), min(m, n)
        for i in range(0, (m-n)//2+1):
            l[n-1+i], l[m-1-i] = l[m-1-i], l[n-1+i]

        head = worker = ListNode(l[0])
        for i in l[1:]:
            worker.next = ListNode(i)
            worker = worker.next
        return head
# ✔ Accepted
#   ✔ 44/44 cases passed (40 ms)
#   ✔ Your runtime beats 45.52 % of python3 submissions
#   ✔ Your memory usage beats 7.41 % of python3 submissions (13.8 MB)
# if __name__ == "__main__":
#     l = [1,2,3,4,5]
#     head = j = ListNode(l[0])
#     for i in l[1:]:
#         j.next = ListNode(i)
#         j = j.next
#     res = Solution().reverseBetween(head, 2, 4)     

