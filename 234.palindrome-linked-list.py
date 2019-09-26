#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h1 = head
        if fast:
            h2 = slow.next
        else:
            h2 = ListNode(slow.val)
            h2.next = slow.next
        slow.next = None

        h2 = self.reverseLinkList(h2)

        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1, h2 = h1.next, h2.next
        return True
    def reverseLinkList(self, head):
        dummy = worker = ListNode(0)
        cur = head
        while cur:
            nxt = cur.next
            cur.next = worker
            worker = cur
            cur = nxt
        head.next = None
        return worker
✔ Accepted
  ✔ 26/26 cases passed (76 ms)
  ✔ Your runtime beats 81.84 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (24.5 MB)
# if __name__ == "__main__":
#     head = ListNode(1)
#     head.next = ListNode(0)
#     head.next.next = ListNode(1)
#     # head.next.next.next = ListNode(1)
#     reverse = Solution().isPalindrome(head)


