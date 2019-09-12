#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        from collections import defaultdict
        if endWord not in wordList: return []
        forward,backward,wordList,dic = {beginWord},{endWord},set(wordList),defaultdict(set)
        flag,letters,length = True,set('qwertyuioplkjhgfdsazxcvbnm'),len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward,backward,flag = backward,forward,not flag
            cur = set()
            wordList -= forward
            for word in forward:
                for idx in range(length):
                    x,y = word[:idx],word[idx+1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in wordList:
                            cur.add(temp)
                            if flag: dic[temp].add(word)
                            else: dic[word].add(temp)  
            if cur & backward:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[x]+y for y in res for x in dic[y[0]]]
                return res
            forward = cur
        return []
# '"qa"\n"sq"\n["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
# "red"\n"tax"\n["ted","tex","red","tax","tad","den","rex","pee"]
# if __name__ == "__main__":
#     beginWord = "hit"
#     endWord = "cog"
#     wordList = ["hot","dot","dog","lot","log","cog"]
#     # wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
#     res = Solution().findLadders(beginWord, endWord, wordList)
#     print(res)

