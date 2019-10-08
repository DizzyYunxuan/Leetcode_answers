#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount < 1: return 0
        return self.memoSearch(coins, amount, {})
    
    def memoSearch(self, coins, rem, memo):
        if rem < 0: return -1
        if rem == 0: return 0
        if rem in memo: return memo[rem]

        minNums = float('inf')
        for c in coins:
            res = self.memoSearch(coins, rem-c, memo)
            if res >= 0:
                minNums = min(1+res, minNums)

        memo[rem] = minNums if minNums != float('inf') else -1
        return memo[rem]
Accepted
182/182 cases passed (2348 ms)
Your runtime beats 5.3 % of python3 submissions
Your memory usage beats 8.33 % of python3 submissions (17.4 MB)
# if __name__ == "__main__":
#     coins = [2]
#     res = Solution().coinChange(coins, 3)
#     print(res)

# @lc code=end

