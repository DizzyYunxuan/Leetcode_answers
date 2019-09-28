#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#
class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
        return n - low
✔ Accepted
  ✔ 84/84 cases passed (168 ms)
  ✔ Your runtime beats 66.72 % of python3 submissions
  ✔ Your memory usage beats 50 % of python3 submissions (20.6 MB)
# if __name__ == "__main__":
#     res = Solution().hIndex([0,1,3,5,6])
