#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def fullJustify(self, words, maxWidth: int):
        num_words, curLen, i , curStr, count = len(words), 0, 0, '', 0  
        res = []         
        while curLen+len(words[i]) <= maxWidth:
                curLen += len(words[i]) + 1
                count += 1
                i += 1
            
if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["Listen","to","many,","speak","to","a","few."]
    # [
    # "Listen ",
    # "to    ",
    # "many, ",
    # "speak ",
    # "to   a",
    # "few.  "
    # ]
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
    res = Solution().fullJustify(words, 6)          
