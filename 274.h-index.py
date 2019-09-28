#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
class Solution:
    def hIndex(self, citations) -> int:
        return sum( i < j for i, j in enumerate(sorted(citations, reverse=True)))
✔ Accepted
  ✔ 82/82 cases passed (44 ms)
  ✔ Your runtime beats 76.75 % of python3 submissions
  ✔ Your memory usage beats 14.29 % of python3 submissions (13.9 MB)


#     def hIndex(self, citations) -> int:
#         if not citations:
#             return 0
#         citations.sort()
#         n = len(citations)
#         res = 0
#         for i in range(n):
#             if citations[i] >= n - i:
#                 res = max(res, n - i)
#         return res
# ✔ Accepted
#   ✔ 82/82 cases passed (44 ms)
#   ✔ Your runtime beats 76.75 % of python3 submissions
#   ✔ Your memory usage beats 14.29 % of python3 submissions (14.1 MB)
# if __name__ == "__main__":
#     res = Solution().hIndex([0])
