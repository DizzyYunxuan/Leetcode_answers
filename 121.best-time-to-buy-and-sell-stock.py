#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices) -> int:
        min_price, max_profit = float('inf'), 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price-min_price)
        return max_profit
✔ Accepted
  ✔ 200/200 cases passed (72 ms)
  ✔ Your runtime beats 78.86 % of python3 submissions
  ✔ Your memory usage beats 5.75 % of python3 submissions (14.9 MB)

