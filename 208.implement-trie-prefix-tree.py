#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = defaultdict(TrieNode)  # Easy to insert new node.
        self.isword = False  # True for the end of the trie.


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            curr = curr.nodes[char]
        curr.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return True
✔ Accepted
  ✔ 15/15 cases passed (208 ms)
  ✔ Your runtime beats 41.23 % of python3 submissions
  ✔ Your memory usage beats 7.41 % of python3 submissions (32.5 MB)
# if __name__ == "__main__":
#     trie = Trie()
#     trie.insert("apple")
#     trie.search("apple") #// returns true
#     trie.search("app")   #// returns false
#     trie.startsWith("app") #// returns true
#     trie.insert("app")   
#     trie.search("app")     #// returns true

# class Trie:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = []

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         self.trie.append(word)

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         return word in self.trie

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         length = len(prefix)
#         for s in self.trie:
#             if s[:length] == prefix:
#                 return True
#         return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

