#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         return sorted(range(1, n+1), key=str)
# Accepted
# 26/26 cases passed (124 ms)
# Your runtime beats 56.41 % of python3 submissions
# Your memory usage beats 97.97 % of python3 submissions (19.3 MB)

class Solution:
    def lexicalOrder(self, n: int):
        highDigit = 1
        while highDigit * 10 <= n:
            highDigit *= 10
        higherDigit = highDigit * 10
        withKeys = []
        for i in range(1, n+1):
            key = i
            while key < highDigit:
                key *= 10
            withKeys.append(key * higherDigit + i)
        withKeys.sort()
        return [ki % higherDigit for ki in withKeys]
 Accepted
26/26 cases passed (116 ms)
Your runtime beats 66.36 % of python3 submissions
Your memory usage beats 58.79 % of python3 submissions (19.8 MB)       
# if __name__ == "__main__":
#     a = Solution().lexicalOrder(100)
#     print(a)


# @lc code=end

