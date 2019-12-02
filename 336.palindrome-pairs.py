#
# @lc app=leetcode id=336 lang=python
#
# [336] Palindrome Pairs
#

# @lc code=start
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {w: i for i, w in enumerate(words)}
        res = []
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)+1):
                pre, suf = w[:j], w[j:]
                if pre[::-1] == pre and suf[::-1] != w and suf[::-1] in d:
                    res.append([d[suf[::-1]], i])
                if suf[::-1] == suf and pre[::-1] != w and pre[::-1] in d and j != len(w):
                    res.append([i, d[pre[::-1]]])
        return res

if __name__ == "__main__":
    l = ["abcd","dcba","lls","s","sssll"]
    res = Solution().palindromePairs(l)
    print(res)


    
# @lc code=end

