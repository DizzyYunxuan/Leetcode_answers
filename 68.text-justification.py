#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def fullJustify(self, words, maxWidth: int):
        num_words, curLen, i , curStr, count = len(words), 0, 0, '', 0  
        res = []  
        while i < num_words:   
            count, curStr, curLen = 0, '', 0    
            while i< num_words and curLen+len(words[i]) <= maxWidth:
                curLen += len(words[i]) + 1
                count += 1
                i += 1
            curLen -= count
            spaces = maxWidth - curLen
            if i < num_words:
                if count == 1:
                    curStr += words[i-1] + spaces * ' '
                    res.append(curStr)

                else:
                    everyspaces = spaces // (count - 1)
                    extraSpaces = spaces % (count - 1)
                    for j in words[i-count:i]:
                        curStr += j 
                        if spaces > 0:   
                            curStr += everyspaces * ' '                        
                            spaces -= everyspaces
                        if extraSpaces:
                            curStr += ' '
                            extraSpaces -= 1
                            spaces -= 1
                    res.append(curStr)
            else:
                for j in words[i-count:i]:
                    curStr += j + ' '
                    spaces -= 1
                curStr = curStr[:-1]
                spaces += 1
                if spaces > 0:
                    curStr += spaces * ' '
                    # spaces -= 
                res.append(curStr)
        return res

                
        
            
# if __name__ == "__main__":
#     words = ["This", "is", "an", "example", "of", "text", "justification."]
    # words = ["Listen","to","many,","speak","to","a","few."]
    # [
    # "Listen ",
    # "to    ",
    # "many, ",
    # "speak ",
    # "to   a",
    # "few.  "
    # ]
    # words = ["Science","is","what","we","understand","well","enough","to","explain",
    #      "to","a","computer.","Art","is","everything","else","we","do"]
    # words = ["What","must","be","acknowledgment","shall","be"]
    # words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
    
    # [
    # "ask   not   what",
    # "your country can",
    # "do  for  you ask",
    # "what  you can do",
    # "for your country "
    # ]

    # [
    # "ask   not   what",
    # "your country can",
    # "do  for  you ask",
    # "what  you can do",
    # "for your country"
    # ]
    # res = Solution().fullJustify(words, 16)          
