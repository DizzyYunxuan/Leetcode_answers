#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
class Solution:
    def isHappy(self, n: int) -> bool:
        memo = {}
        while n != 1:
            exp, t = 0, 0
            while n // (10**exp):
                t += (n % (10**(exp+1)) // (10**exp))**2
                exp += 1
            if t in memo:
                return False
            memo[t] = 1
            n = t
        return True
✔ Accepted
  ✔ 401/401 cases passed (48 ms)
  ✔ Your runtime beats 15.5 % of python3 submissions
  ✔ Your memory usage beats 5.26 % of python3 submissions (13.6 MB)
# if __name__ == "__main__":
#     res = Solution().isHappy(19)     

