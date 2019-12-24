#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def qpow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m     
            n >>= 1
        return ans    
        
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.qpow(res, 10, 1337) * self.qpow(a, i, 1337)
        return res % 1337



#     def superPow(self, a: int, b) -> int:
#         return pow(a, int(''.join(map(str, b))), 1337)
# Accepted
# 54/54 cases passed (88 ms)
# Your runtime beats 95.24 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# if __name__ == "__main__":
#     res = Solution().superPow(2, [1,0])
#     print(res)



# @lc code=end

