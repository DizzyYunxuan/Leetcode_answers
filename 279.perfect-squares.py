#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
class Solution:
    def numSquares(self, n: int) -> int:
        if int(n**0.5)**2 == n: return 1
        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7:
            return 4
        maxsq = int(n ** 0.5) + 1
        for i in range(1, maxsq):
            if int((n-i*i)**0.5)**2 == n - i*i:
                return 2       
        return 3
✔ Accepted
  ✔ 588/588 cases passed (40 ms)
  ✔ Your runtime beats 98.07 % of python3 submissions
  ✔ Your memory usage beats 60 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     res = Solution().numSquares(28)
