#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails , res = [0] * len(nums), 0
        for n in nums:
            low, high = 0, res
            while low < high:
                mid = (low + high) // 2
                if tails[mid] < n:
                    low = mid + 1
                else:
                    high = mid
            tails[low] = n
            if high == res:
                res += 1
        return res
Accepted
24/24 cases passed (52 ms)
Your runtime beats 79.12 % of python3 submissions
Your memory usage beats 5.13 % of python3 submissions (13.9 MB)       
# @lc code=end

