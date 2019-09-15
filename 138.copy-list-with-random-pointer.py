#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# Definition for a Node.
# class Node:
#     def __init__(self, val, next, random):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        d = {head: Node(head.val, None, None)}
        worker = head
        while worker:
            if worker not in d:
                d[worker] = Node(worker.val, None, None)
            if worker.next and worker.next not in d:
                d[worker.next] = Node(worker.next.val, None, None)
            elif not worker.next:
                d[worker.next] = None
            if worker.random and worker.random not in d:
                d[worker.random] = Node(worker.random.val, None, None)
            elif not worker.random:
                d[worker.random] = None
            d[worker].next = d[worker.next]
            d[worker].random = d[worker.random]
            worker = worker.next
        return d[head]
✔ Accepted
  ✔ 9/9 cases passed (36 ms)
  ✔ Your runtime beats 99.77 % of python3 submissions
  ✔ Your memory usage beats 6.98 % of python3 submissions (16 MB)

# if __name__ == "__main__":
#     node1 = Node(1, None, None)
#     node2 = Node(2, None, None)
#     node1.next = node2
#     node1.random = node2
#     node2.random = node2
#     res = Solution().copyRandomList(node1)
