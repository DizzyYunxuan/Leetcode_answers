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
        l[n-1:m] = l[m-1:n-2:-1]
        head = worker = ListNode(l[0])
        for i in l[1:]:
            worker.next = ListNode(i)
            worker = worker.next
        return head
        
        
        

if __name__ == "__main__":
    l = [5]
    head = j = ListNode(l[0])
    for i in l[1:]:
        j.next = ListNode(i)
        j = j.next
    res = Solution().reverseBetween(head, 1, 2)     

