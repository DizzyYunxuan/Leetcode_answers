#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        import itertools
        import heapq
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u*p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        map(uglies.append, itertools.islice(uniqed, n-1))
        return uglies[-1]







if __name__ == "__main__":
    res = Solution().nthSuperUglyNumber(12, [2,7,13,19])


#     def nthSuperUglyNumber(self, n: int, primes) -> int:
#         np = len(primes)
#         dp = [float('inf')] * n
#         dp[0] = 1
#         idxes = [0] * len(primes)
#         for i in range(1, n):
#             for j in range(np):
#                 dp[i] = min(dp[idxes[j]]*primes[j], dp[i])
#             for j in range(np):
#                 if dp[i] / dp[idxes[j]] == primes[j]:
#                     idxes[j] += 1
#         return dp[-1]


# Accepted
# 83/83 cases passed (1432 ms)
# Your runtime beats 5.19 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (17.8 MB)


# @lc code=end

