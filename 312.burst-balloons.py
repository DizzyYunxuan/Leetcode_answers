#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums) -> int:
        if nums is None:
                return 0
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for window in range(1, n-1):
            for start in range(1, n-window):
                for k in range(start, start+window):
                    dp[start][start+window-1] = \
                        max(dp[start][start+window-1], \
                            nums[start-1]*nums[k]*nums[start+window]+dp[start][k-1]+dp[k+1][start+window-1])
        return dp[1][n-2]
Accepted
70/70 cases passed (608 ms)
Your runtime beats 33.95 % of python3 submissions
Your memory usage beats 25 % of python3 submissions (14.3 MB)
# if __name__ == "__main__":
#     res = Solution().maxCoins([3,1,5,8])
# @lc code=end

