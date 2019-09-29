#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.temp
        

    def next(self):
        """
        :rtype: int
        """
        r = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return r

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.temp is not None
        
✔ Accepted
  ✔ 13/13 cases passed (36 ms)
  ✔ Your runtime beats 84.48 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (13.7 MB)
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

