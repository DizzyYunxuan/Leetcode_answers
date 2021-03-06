#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        if n:
           dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]
✔ Accepted
  ✔ 19/19 cases passed (36 ms)
  ✔ Your runtime beats 66.44 % of python3 submissions
  ✔ Your memory usage beats 10.71 % of python3 submissions (14 MB)
            
# if __name__ == "__main__":
#     res = Solution().numTrees(4)
#     print(res)



