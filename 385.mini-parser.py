#
# @lc app=leetcode id=385 lang=python3
#
# [385] Mini Parser
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#        self.l = [value] if value else []

#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#        pass

#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#        self.l = [elem] + self.l

#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#        pass
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#        pass

#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
#        pass

class Solution:
    def deserialize(self, s: str):
        s = list(' ' + s[::-1])
        res = self.nestedInteger(s)
        return res
        

    def nestedInteger(self, s):
        num = ''
        while s[-1] in '1234567890-':
            num += s.pop()
        if num:
            return NestedInteger(int(num))
        s.pop()
        lst = NestedInteger()
        while s[-1] != ']':
            lst.add(self.nestedInteger(s))
            if s[-1] == ',':
                s.pop()
        s.pop()
        return lst
        
Accepted
57/57 cases passed (140 ms)
Your runtime beats 6.08 % of python3 submissions
Your memory usage beats 22.22 % of python3 submissions (17.2 MB)
# s = "[-1]"
# a = Solution().deserialize(s)
# print()
# @lc code=end

