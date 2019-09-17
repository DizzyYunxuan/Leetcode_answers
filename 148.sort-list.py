#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        res = self.split_merge(head)
        return res
    
    def split_merge(self, head):
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l, r = self.split_merge(head), self.split_merge(mid)
        merged = self.merge(l,r)
        return merged
    
    def merge(self, head, mid):
        dummy = worker = ListNode(0)
        while head and mid:
            if head.val <= mid.val:
                worker.next = head
                head = head.next
                worker = worker.next
                worker.next = None
            else:
                worker.next = mid
                mid = mid.next
                worker = worker.next
                worker.next = None
        worker.next = head or mid
        return dummy.next
✔ Accepted
  ✔ 16/16 cases passed (264 ms)
  ✔ Your runtime beats 23.64 % of python3 submissions
  ✔ Your memory usage beats 15.38 % of python3 submissions (21.3 MB)

# if __name__ == "__main__":
#     a = ListNode(1)
#     a.next = ListNode(3)
#     a.next.next = ListNode(5)

#     b = ListNode(2)
#     b.next = ListNode(4)
#     b.next.next = ListNode(6)
#     b.next.next.next = ListNode(8)
#     a.next.next.next = b
#     res = Solution().sortList(a)
