#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
class Solution:
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
    

# if __name__ == "__main__":
#     board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#     words = ["oath","pea","eat","rain"]

#     res = Solution().findWords(board, words)

