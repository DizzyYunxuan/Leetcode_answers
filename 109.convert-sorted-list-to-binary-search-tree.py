#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


#     def sortedListToBST(self, head: ListNode) -> TreeNode:
#         worker, l = head, []
#         while worker:
#             l.append(worker.val)
#             worker = worker.next
#         return self.sortedArrayToBST(l)

#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#         idx = len(nums) // 2
#         root = TreeNode(nums[idx])
#         root.left = self.sortedArrayToBST(nums[:idx])
#         root.right = self.sortedArrayToBST(nums[idx+1:])
#         return root
# ✔ Accepted
#   ✔ 32/32 cases passed (136 ms)
#   ✔ Your runtime beats 63.99 % of python3 submissions
#   ✔ Your memory usage beats 6.67 % of python3 submissions (20.5 MB)
