#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
class Solution:
    def findWords(self, board, words):
        prefixTree = {'isEndOfWord':False}
        for w in words:
            curn = prefixTree
            for c in w:
                curn[c] = curn.get(c, {})
                curn = curn[c]
                curn['isEndOfWord'] = curn.get('isEndOfWord', False)
            curn['isEndOfWord'] = True
        self.res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in prefixTree:
                    self.dfsOnPrefixTree(board, [i, j], prefixTree, '')
        return self.res

    def dfsOnPrefixTree(self, board, pos, root, path):
        x, y = pos
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return 
        if root.get(board[x][y], None):
            if root[board[x][y]]['isEndOfWord'] == True:
                self.res.append(path+board[x][y])
                root[board[x][y]]['isEndOfWord'] = False
            memo = board[x][y]
            board[x][y] = '-'
            directions = [[x-1,y],[x+1,y],[x, y-1], [x,y+1]]
            for d in directions:
                self.dfsOnPrefixTree(board, d, root[memo], path+memo) 
            board[x][y] = memo
✔ Accepted
  ✔ 36/36 cases passed (448 ms)
  ✔ Your runtime beats 35.82 % of python3 submissions
  ✔ Your memory usage beats 91.67 % of python3 submissions (28.1 MB)
        
# if __name__ == "__main__":
#     board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#     words = ["oath","pea","eat","rain"]
#     board = [["a","b"],["c","d"]]
#     words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
#     res = Solution().findWords(board, words)

############################   DFS TLE   #############################
'''   
    def findWords(self, board, words):
        res = []
        for w in words:
            flag = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.dfs(w, [i,j], board):
                        flag = True
                        res.append(w)
                        break
                if flag:
                    break
        return res

    
    def dfs(self, word, pos, board):
        if not word:
            return True
        x, y = pos
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if board[x][y] == word[0]:
            memo = board[x][y]
            board[x][y] = '-'
            directions = [[x-1,y],[x+1,y],[x, y-1], [x,y+1]]
            for d in directions:
                if self.dfs(word[1:], d, board):
                    board[x][y] = memo
                    return True
            board[x][y] = memo
            return False
        else:
            return False
'''  



