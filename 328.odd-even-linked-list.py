#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd, even, ehead = head, head.next, head.next
        worker, odd.next, even.next = even.next, None, None
        while worker and worker.next:
            odd.next, even.next = worker, worker.next
            odd, even = odd.next, even.next
            worker.next = None
            worker = even.next
            even.next = None
        if worker:
            odd.next = worker
            odd = odd.next
        odd.next = ehead
        return head
Accepted
71/71 cases passed (52 ms)
Your runtime beats 48.62 % of python3 submissions
Your memory usage beats 8.33 % of python3 submissions (15.6 MB)
# if __name__ == "__main__":
#     head = ListNode(1)
#     worker = head
#     for i in range(2, 6):
#         worker.next = ListNode(i) 
#         worker = worker.next
#     res = Solution().oddEvenList(head)

# @lc code=end

