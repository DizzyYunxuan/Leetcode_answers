#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s: return s
        vowels = 'aeiou'
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i != j and s[i].lower() not in vowels:
                i += 1
            while i != j and s[j].lower() not in vowels:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)
Accepted
481/481 cases passed (52 ms)
Your runtime beats 85.79 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.7 MB)


# if __name__ == "__main__":
#     res = Solution().reverseVowels('aA')
# @lc code=end

