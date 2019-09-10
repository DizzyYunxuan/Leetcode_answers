#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution:
    def maxProfit(self, prices) -> int:
        profit, max_profit, min_price = [], 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
            profit.append(max_profit)
        
        max_profit, max_price = 0, float('-inf')
        res = 0
        for i in range(len(prices)-1, -1, -1):
            max_price = max(prices[i], max_price)
            max_profit = max(max_profit, max_price-prices[i])
            res = max(res, max_profit+profit[i])
        return res
# ✔ Accepted
#   ✔ 200/200 cases passed (88 ms)
#   ✔ Your runtime beats 69.86 % of python3 submissions
#   ✔ Your memory usage beats 54.55 % of python3 submissions (15 MB)
if __name__ == "__main__":
    res = Solution().maxProfit([1,2,4,2,5,7,2,4,9,0])
    print(res)
