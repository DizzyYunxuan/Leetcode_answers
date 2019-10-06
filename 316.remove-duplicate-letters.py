#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        counts = Counter(s)
        res = ['0']
        for c in s:
            if c not in res:
                while c < res[-1] and counts[res[-1]]:
                    res.pop()
                res.append(c)
            counts[c] -= 1
        return ''.join(res[1:])
Accepted
286/286 cases passed (64 ms)
Your runtime beats 20.43 % of python3 submissions
Your memory usage beats 14.29 % of python3 submissions (14 MB)
# if __name__ == "__main__":
#     res = Solution().removeDuplicateLetters("bcabc")
# @lc code=end

