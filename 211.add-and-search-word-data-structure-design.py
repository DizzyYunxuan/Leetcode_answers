#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

class PrefixTree:
    def __init__(self):
        self.nextnodes = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = PrefixTree()

        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curc = self.root
        for c in word:
            curc.nextnodes[c] = curc.nextnodes.get(c, PrefixTree())
            curc = curc.nextnodes[c]
        curc.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfssearch(word, self.root)

    def dfssearch(self, word, root):
        if not word:
            if root.isEndOfWord:
                return True
            else:
                return False
        
        if word[0] == '.':
            for nxc in root.nextnodes:
                if self.dfssearch(word[1:], root.nextnodes[nxc]):
                    return True
            return False
        else:
            if root.nextnodes.get(word[0], None):
                return self.dfssearch(word[1:], root.nextnodes[word[0]])
            else:
                return False
   ✔ Accepted
  ✔ 13/13 cases passed (448 ms)
  ✔ Your runtime beats 19.34 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (29.8 MB) 
# if __name__ == "__main__":
#     pretree = WordDictionary()
#     pretree.addWord("bad")
#     pretree.addWord("dad")
#     pretree.addWord("mad")
#     pretree.search("pad")
#     pretree.search("bad")
#     pretree.search(".ad")
#     pretree.search("b..") 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

