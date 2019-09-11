#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        self.res = float('inf')
        self.solver(beginWord, endWord, wordList, 0)
        return 0 if self.res == float('inf') else self.res
    def solver(self, begin, end, wordlist, path):
        if begin == end:
            self.res = min(self.res, path+1)
        stack = self.canchange(begin, wordlist)
        for i in stack:
            idx = wordlist.index(i)
            self.solver(i, end, wordlist[:idx]+wordlist[idx+1:], path+1)

    def canchange(self, word, wordlist):
        canchangelist = []
        for cword in wordlist:
            for i in range(len(word)):
                t = word[:i] + cword[i] + word[i+1:]
                if t == cword and t != word:
                    canchangelist.append(cword)
        return canchangelist

# if __name__ == "__main__":
#     # beginWord = "hit"
#     beginWord = "hot"
#     # endWord = "cog"
#     endWord = "dog"
#     wordlist = ["hot","dot","dog","lot","log","cog"]
#     wordlist = ["hot","dog"]
#     res = Solution().ladderLength(beginWord, endWord, wordlist)
#     print(res)
