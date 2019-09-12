#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        self.wdict = {}
        self.builddict(wordList)
        self.visited = {}
        res = self.solver(beginWord, endWord)
        return 0 if not res else res
    
    def solver(self, begin, end):
        self.visited[begin] = True
        stack = [(begin, 1)]
        while stack:
            cur, level = stack.pop(0)
            for i in range(len(begin)):
                inter = cur[:i]+'*'+cur[i+1:]
                if inter in self.wdict:
                    for i in self.wdict[inter]:
                        if i == end:
                            return level+1 
                        if i not in self.visited:
                            stack.append((i, level+1))
                            self.visited[i] = True
                    self.wdict[inter] = []
         
    def builddict(self, wordlist):
        for word in wordlist:
            for i in range(len(word)):
                if word[:i]+'*'+word[i+1:] not in self.wdict:
                    self.wdict[word[:i]+'*'+word[i+1:]] = [word]
                else:
                    self.wdict[word[:i]+'*'+word[i+1:]].append(word)
# ✔ Accepted
#   ✔ 40/40 cases passed (148 ms)
#   ✔ Your runtime beats 62.17 % of python3 submissions
#   ✔ Your memory usage beats 6.9 % of python3 submissions (17.3 MB)


# from collections import defaultdict
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """

#         if endWord not in wordList or not endWord or not beginWord or not wordList:
#             return 0

#         # Since all words are of same length.
#         L = len(beginWord)

#         # Dictionary to hold combination of words that can be formed,
#         # from any given word. By changing one letter at a time.
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 # Key is the generic word
#                 # Value is a list of words which have the same intermediate generic word.
#                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


#         # Queue for BFS
#         queue = [(beginWord, 1)]
#         # Visited to make sure we don't repeat processing same word.
#         visited = {beginWord: True}
#         while queue:
#             current_word, level = queue.pop(0)      
#             for i in range(L):
#                 # Intermediate words for current word
#                 intermediate_word = current_word[:i] + "*" + current_word[i+1:]

#                 # Next states are all the words which share the same intermediate state.
#                 for word in all_combo_dict[intermediate_word]:
#                     # If at any point if we find what we are looking for
#                     # i.e. the end word - we can return with the answer.
#                     if word == endWord:
#                         return level + 1
#                     # Otherwise, add it to the BFS Queue. Also mark it visited
#                     if word not in visited:
#                         visited[word] = True
#                         queue.append((word, level + 1))
#                 all_combo_dict[intermediate_word] = []
#         return 0
# ✔ Accepted
#   ✔ 40/40 cases passed (132 ms)
#   ✔ Your runtime beats 76.31 % of python3 submissions
#   ✔ Your memory usage beats 6.9 % of python3 submissions (17.2 MB)
# if __name__ == "__main__":
#     beginWord = "hit"
#     # beginWord = "hot"
#     endWord = "cog"
#     # endWord = "dog"
#     wordlist = ["hot","dot","dog","lot","log","cog"]
#     # wordlist = ["hot","dog"]
#     res = Solution().ladderLength(beginWord, endWord, wordlist)
#     print(res)
