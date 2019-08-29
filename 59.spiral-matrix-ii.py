#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
class Solution:
    def generateMatrix(self, n: int):
        res = []
        start, end = n*n, n*n+1
        while start > 0:
            cur = [i for i in range(start, end)]
            res = [cur] + list(zip(*res[::-1]))
            end = start
            start = end - len(res)
        return res
        
✔ Accepted
  ✔ 20/20 cases passed (40 ms)
  ✔ Your runtime beats 56.54 % of python3 submissions
  ✔ Your memory usage beats 9.09 % of python3 submissions (13.9 MB)    
# if __name__ == "__main__":
#     res = Solution().generateMatrix(3)
