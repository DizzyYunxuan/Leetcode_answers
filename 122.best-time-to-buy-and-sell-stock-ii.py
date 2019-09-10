#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i] > 0:
                profit += prices[i+1]-prices[i]
        return profit
 ✔ Accepted
  ✔ 201/201 cases passed (68 ms)
  ✔ Your runtime beats 90.07 % of python3 submissions
  ✔ Your memory usage beats 7.32 % of python3 submissions (14.8 MB)       

