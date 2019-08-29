#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals):
        if not intervals:
            return 
        # intervals = self.bbsort(intervals)
        intervals.sort()
        res, t = [], intervals[0].copy()
        for i in range(1, len(intervals)):
            if intervals[i][0] > t[1]:
                res.append(t)
                t = intervals[i]
            else:
                t[1] = max(intervals[i][1], t[1])     
        res.append(t)  
        return res
    def bbsort(self, intervals):
        for tail in range(len(intervals)):
            i = len(intervals) - 1
            while i > tail:
                if intervals[i][0] < intervals[i-1][0]:
                    intervals[i], intervals[i-1] = intervals[i-1], intervals[i]
                i -= 1
        return intervals
✔ Accepted
  ✔ 169/169 cases passed (100 ms)
  ✔ Your runtime beats 74.93 % of python3 submissions
  ✔ Your memory usage beats 6.52 % of python3 submissions (15.7 MB)
# if __name__ == "__main__":
#     res = Solution().merge([[1,3],[2,6],[15,18], [8,10]])    

