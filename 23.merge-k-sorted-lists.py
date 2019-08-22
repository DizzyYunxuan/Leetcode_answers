#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None
        res = lists[0]
        for i in lists[1:]:
            res = self.sort2(res, i)
        return res
    def sort2(self, l1, l2):
        r = ListNode(0)
        t = r
        while l1 and l2:
            if l1.val >= l2.val:
                t.next = l2
                l2 = l2.next
            else:
                t.next = l1
                l1 = l1.next
            t = t.next
        if l1:
            t.next = l1
        elif l2:
            t.next = l2
        return r.next

✔ Accepted
  ✔ 131/131 cases passed (4560 ms)
  ✔ Your runtime beats 10.96 % of python3 submissions
  ✔ Your memory usage beats 27.27 % of python3 submissions (17.2 MB)


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        t = []
        for i in lists:
            cur = i
            while cur:
                t.append(cur.val)
                cur = cur.next
        t.sort()
        res = ListNode(0)
        j = res
        for i in t:
            j.next = ListNode(i)
            j = j.next
        return res.next
✔ Accepted
  ✔ 131/131 cases passed (108 ms)
  ✔ Your runtime beats 87.75 % of python3 submissions
  ✔ Your memory usage beats 12.12 % of python3 submissions (17.8 MB)
