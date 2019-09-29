#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.nums, self.length = [], 0


    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        self.length += 1
        

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            return (self.nums[self.length//2-1] + self.nums[self.length//2]) / 2
        else:
            return self.nums[self.length//2]

✔ Accepted
  ✔ 18/18 cases passed (260 ms)
  ✔ Your runtime beats 18.58 % of python3 submissions
  ✔ Your memory usage beats 6.67 % of python3 submissions (24.8 MB)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

