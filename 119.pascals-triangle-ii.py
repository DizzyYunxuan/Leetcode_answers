#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    def getRow(self, rowIndex: int):
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal
 ✔ Accepted
  ✔ 34/34 cases passed (36 ms)
  ✔ Your runtime beats 75.72 % of python3 submissions
  ✔ Your memory usage beats 7.69 % of python3 submissions (13.8 MB)       
#     def getRow(self, rowIndex: int):
#         res = [self.calculateC(rowIndex, k) for k in range(rowIndex+1)]
#         return res
    
#     def calculateC(self, m, k):
#         k = m - k if k > m - k else k
#         upper = under = 1
#         for _ in range(k):
#             upper *= m
#             under *= k
#             m -= 1
#             k -= 1
#         return upper // under
# ✔ Accepted
#   ✔ 34/34 cases passed (36 ms)
#   ✔ Your runtime beats 75.72 % of python3 submissions
#   ✔ Your memory usage beats 7.69 % of python3 submissions (13.8 MB)     

# if __name__ == "__main__":
#     res = Solution().getRow(5)
#     print(res)
