#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        count1, count2 = 0, 0
        while p1:
            p1 = p1.next
            count1 += 1
        while p2:
            p2 = p2.next
            count2 += 1
        sub = count1 - count2
        p1, p2 = headA, headB
        if sub > 0:
            while sub > 0:
                p1 = p1.next
                sub -= 1
        else:
            while sub < 0:
                p2 = p2.next
                sub += 1
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1 if p1 else None
✔ Accepted
  ✔ 45/45 cases passed (180 ms)
  ✔ Your runtime beats 95.62 % of python submissions
  ✔ Your memory usage beats 40 % of python submissions (41.8 MB)
