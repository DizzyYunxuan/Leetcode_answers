#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A, B = 0, 0
        ds = {}
        dg = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                ds[secret[i]] = ds.get(secret[i], 0) + 1
                dg[guess[i]] = dg.get(guess[i], 0) + 1
        for g in dg:
            if ds.get(g, 0):
                B += min(ds[g], dg[g])
        return str(A)+'A'+str(B)+'B'
Accepted
    152/152 cases passed (48 ms)
    Your runtime beats 66.8 % of python3 submissions
    Your memory usage beats 25 % of python3 submissions (13.8 MB)


# if __name__ == "__main__":
#     res = Solution().getHint("1123", "0111")
#     print(res)
# @lc code=end

