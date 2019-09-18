class Solution():
    def __init__(self):
        self.shortest = float('inf')
    
    def jungle(self, valley):
        monsters = {}
        for i in range(len(valley)):
            for j in range(len(valley[0])):
                if valley[i][j] != '-' and valley[i][j] > 0:
                    monsters[valley[i][j]] = (i, j)
        curx, cury = 0, 0
        length = 0
        while monsters:
            self.shortest = float('inf')
            monsterWanted = monsters.pop(min(monsters.keys()))
            self.findpath((curx, cury), monsterWanted, 0, valley)
            length += self.shortest
            curx, cury = monsterWanted
        return length
    def findpath(self, start, end, path, valley):
        if start == end:
            self.shortest = min(self.shortest, path)
            return
        x, y = start[0], start[1]
        if x < 0 or x >= len(valley) or y < 0 or y >= len(valley[0]) or valley[x][y] == '-':
            return
        directions = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        memo = valley[x][y]
        valley[x][y] = '-'
        for direc in directions:
            self.findpath(direc, end, path+1, valley)
        valley[x][y] = memo
if __name__ == "__main__":
    valley = [[1,2,3],['-','-',4],[7,6,5]]
    shortest = float('inf')
    tes = Solution().jungle(valley)
    x = 1
 