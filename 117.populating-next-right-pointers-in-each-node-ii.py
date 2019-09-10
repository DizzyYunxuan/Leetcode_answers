#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        res = []
        self.sovler(root, 0, res)
        for i in res:
            for j in range(len(i)-1):
                i[j].next = i[j+1]
        return root
    def sovler(self, root, depth, res):
        if not root:
            return
        if depth+1 > len(res):
            res.append([root])
        else:
            res[depth].append(root)
        self.sovler(root.left, depth+1, res)
        self.sovler(root.right, depth+1, res)
✔ Accepted
  ✔ 55/55 cases passed (388 ms)
  ✔ Your runtime beats 76.28 % of python3 submissions
  ✔ Your memory usage beats 8.33 % of python3 submissions (48.4 MB)

    def connect(self, root: 'Node') -> 'Node':
        ori = root
        tail = dummy = Node(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next
        return ori
✔ Accepted
  ✔ 55/55 cases passed (404 ms)
  ✔ Your runtime beats 23.32 % of python3 submissions
  ✔ Your memory usage beats 8.33 % of python3 submissions (48.6 MB)


