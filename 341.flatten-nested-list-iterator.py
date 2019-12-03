#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nl = nestedList
    def next(self) -> int:
        return self.nl.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        if len(self.nl) == 0:
            return False
        else:
            while len(self.nl) and not self.nl[0].isInteger():
                self.nl = self.nl.pop(0).getList() + self.nl 
            if not len(self.nl):
                return False
        return len(self.nl)

Accepted
44/44 cases passed (56 ms)
Your runtime beats 100 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (16.4 MB)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

