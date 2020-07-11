#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.count = 0
        worker = head
        while worker:
            worker = worker.next
            self.count += 1
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        rand = random.randint(0, self.count - 1)
        worker = self.head
        while rand:
            worker = worker.next
            rand -= 1
        return worker.val
        
Accepted
7/7 cases passed (88 ms)
Your runtime beats 80 % of python3 submissions
Your memory usage beats 81.48 % of python3 submissions (17 MB)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

