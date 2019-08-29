#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        i, res = head, []
        while i:
            res.append(i.val)
            i = i.next
        k %= len(res) 
        res = res[len(res)-k:] + res[:len(res)-k]
        head = ListNode(res[0])
        t = head
        for i in res[1:]:
            t.next = ListNode(i)
            t= t.next
        return head
✔ Accepted
  ✔ 231/231 cases passed (44 ms)
  ✔ Your runtime beats 59.82 % of python3 submissions
  ✔ Your memory usage beats 6.45 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     head = ListNode(1)
#     t = head
#     for i in range(2, 6):    
#         t.next = ListNode(i)
#         t = t.next
#     res = Solution().rotateRight(head, 2)     
        
