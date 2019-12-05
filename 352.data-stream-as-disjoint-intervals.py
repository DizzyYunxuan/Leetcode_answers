#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#

# @lc code=start
# class SummaryRanges:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.l = []

#     def addNum(self, val: int) -> None:
#         low, high = 0, len(self.l)-1
#         while low <= high:
#             mid = (low + high) // 2
#             if self.l[mid] == val:
#                 return
#             elif val < self.l[mid]:
#                 high = mid - 1
#             elif val > self.l[mid]:
#                 low = mid + 1
#         self.l.insert(low, val)

#     def getIntervals(self):
#         intervals = []
#         start, i = 0, 1
#         while start < len(self.l):
#             while i < len(self.l) and self.l[i] - self.l[i-1] == 1:   
#                 i += 1
#             intervals.append([self.l[start], self.l[i-1]])
#             start = i
#             i = start + 1
#         return intervals

# Accepted
# 9/9 cases passed (896 ms)
# Your runtime beats 5.05 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (17.2 MB)




class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def addNum(self, val: int) -> None:
        low, high = 0, len(self.l) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.l[mid][0] <= val <= self.l[mid][1]:
                return
            elif val > self.l[mid][0]:
                low = mid + 1
            elif val < self.l[mid][0]:
                high = mid - 1
        if low >= len(self.l):
            if self.l and self.l[low-1][1] + 1 == val:
                self.l[low-1][1] = val
            else:
                self.l.append([val, val])
        else:
            if low == 0:
                if self.l and self.l[low][0] - 1 == val:
                    self.l[low][0] = val
                else:
                    self.l.insert(low, [val, val])
            else:
                if self.l[low-1][1] + 1 == val and val + 1 == self.l[low][0]:
                    self.l[low-1:low+1] = [[self.l[low-1][0], self.l[low][1]]]
                elif self.l[low-1][1] + 1 == val:
                    self.l[low-1][1] = val
                elif self.l[low][0] - 1 == val:
                    self.l[low][0] = val
                else:
                    self.l.insert(low, [val, val])
    def getIntervals(self):
        return self.l

Accepted
9/9 cases passed (152 ms)
Your runtime beats 99.04 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (17.3 MB)



# if __name__ == "__main__":
#     obj = SummaryRanges()
#     obj.addNum(0)
#     param_2 = obj.getIntervals()
#     obj.addNum(1)
#     param_2 = obj.getIntervals()
    # obj.addNum(7)
    # param_2 = obj.getIntervals()
    # obj.addNum(2)
    # param_2 = obj.getIntervals()
    # obj.addNum(6)
    # param_2 = obj.getIntervals()
#     # obj.addNum(10)
#     # param_2 = obj.getIntervals()
#     print(1)
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

