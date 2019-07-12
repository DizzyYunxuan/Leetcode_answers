#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        p = l1
        q = l2
        l3 = ListNode(0)
        z = l3
        while p and q:     
            z.val = (p.val + q.val + carry) % 10
            carry = (p.val + q.val + carry) // 10
            if p.next != None or q.next != None:
                z.next = ListNode(0)
                z = z.next
            elif carry != 0:
                z.next = ListNode(carry)
                return l3
            else:
                return l3
            p = p.next
            q = q.next


        while p:
            z.val = (p.val + carry) % 10
            carry = (p.val + carry) // 10
            if p.next != None:
                z.next = ListNode(0)
                z = z.next
            elif carry != 0:
                z.next = ListNode(carry)
                return l3
            else:
                return l3
            p = p.next



        while q:
            z.val = (q.val + carry) % 10
            carry = (q.val + carry) // 10
            if q.next != None:
                z.next = ListNode(0)
                z = z.next
            elif carry != 0:
                z.next = ListNode(carry)
                return l3
            else:
                return l3
            q = q.next

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         a, b = 0, 0
#         p, q = l1, l2
#         i = 1
#         while p:
#             a += p.val * i
#             i *= 10
#             p = p.next
        
#         i = 1
#         while q:
#             b += q.val * i
#             i *= 10
#             q = q.next
        
#         res = str(a+b)
#         l3 = ListNode(0)
#         z = l3
#         for i in range(len(res) - 1, -1, -1):
#             z.val = int(res[i])
#             if i  == 0:
#                 break
#             z.next = ListNode(0)
#             z = z.next 
        
#         return l3
        #✔ Accepted
            # ✔ 1563/1563 cases passed (56 ms)
            # ✔ Your runtime beats 77.74 % of python submissions
            # ✔ Your memory usage beats 45.85 % of python submissions (11.9 MB)


