#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
class Solution:
    def findSubstring(self, s: str, words):
        s_split = []
        for i in range(0, len(s), 3):
            s_split.append(s[i:i+3])
        
if __name__ == '__main__':
    res = Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
    print(res)


