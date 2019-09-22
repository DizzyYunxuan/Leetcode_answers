#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        res = [1] * n
        res[0], res[1] = 0, 0
        for i in range(2, n):
            if res[i] == 1:
                for j in range(2, (n-1)//i+1):
                    res[i*j] = 0
        return sum(res)

✔ Accepted
  ✔ 20/20 cases passed (924 ms)
  ✔ Your runtime beats 31 % of python3 submissions
  ✔ Your memory usage beats 79.31 % of python3 submissions (25.3 MB)
# if __name__ == "__main__":
#     res = Solution().countPrimes(10)
#     print(res)

