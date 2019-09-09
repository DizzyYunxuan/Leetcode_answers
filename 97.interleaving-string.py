#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1+l2 != l3:
            return False
        dp = [[0] * (l1+1) for _ in range(l2+1)]
        dp[0][0] = 1
        for i in range(1, l1+1):
            if s1[:i] == s3[:i]:
                dp[0][i] = 1
        for i in range(1, l2+1):
            if s2[:i] == s3[:i]:
                dp[i][0] = 1
        
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if dp[i-1][j] == 1 and s2[i-1] == s3[i+j-1]:
                    dp[i][j] = 1
                elif dp[i][j-1] == 1 and s1[j-1] == s3[i+j-1]:
                    dp[i][j] = 1                   
        return dp[-1][-1]

✔ Accepted
  ✔ 101/101 cases passed (40 ms)
  ✔ Your runtime beats 81.19 % of python3 submissions
  ✔ Your memory usage beats 16.67 % of python3 submissions (14 MB)


# if __name__ == "__main__":
#     s1, s2, s3 = "a", "b", "a"
#     res = Solution().isInterleave(s1, s2, s3)
