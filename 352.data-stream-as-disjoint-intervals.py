#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def addNum(self, val: int) -> None:
        low, high = 0, len(self.l)
        while low < high:
            mid = (low + high) // 2
            if self.l[mid][0] <= val <= self.l[mid][1]:
                return
            elif val < self.l[mid][0]:
                
            elif val > self.l[mid][1]:



    def getIntervals(self) -> List[List[int]]:
        pass


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

