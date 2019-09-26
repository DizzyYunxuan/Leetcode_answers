#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack = [x] + self.stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack
✔ Accepted
  ✔ 17/17 cases passed (36 ms)
  ✔ Your runtime beats 63.74 % of python3 submissions
  ✔ Your memory usage beats 10 % of python3 submissions (13.7 MB)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

