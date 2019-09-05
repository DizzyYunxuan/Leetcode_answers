#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l, i = [], head
        while i:
            l.append(i.val)
            i = i.next
        end_of_left = 0
        for i in range(len(l)):
            if l[i] < x:
                l.insert(end_of_left, l[i])
                l.pop(i+1)
                end_of_left += 1
        newhead = ListNode(0)
        i = newhead
        for j in l:
            i.next = ListNode(j)
            i = i.next
        return newhead.next
✔ Accepted
  ✔ 166/166 cases passed (36 ms)
  ✔ Your runtime beats 91.82 % of python3 submissions
  ✔ Your memory usage beats 5 % of python3 submissions (13.8 MB)



    def partition(self, head: ListNode, x: int) -> ListNode:
        left, right = ListNode(-1), ListNode(-1)
        l, r = left, right
        i = head
        while i:
            j = i
            if i.val < x:
                l.next = i
                l = l.next
            else:
                r.next = i
                r = r.next
            i = i.next
            j.next = None
        l.next = right.next
        return left.next
✔ Accepted
  ✔ 166/166 cases passed (28 ms)
  ✔ Your runtime beats 99.8 % of python3 submissions
  ✔ Your memory usage beats 5 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     l, head = [1,4,3,2,5,2], ListNode(1)
#     i = head
#     for j in l[1:]:
#         i.next = ListNode(j)
#         i = i.next
#     res = Solution().partition(head, 3)
        

