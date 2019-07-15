#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1 or numRows >= len(s):
    #         return s
    #     res = [''] * numRows
    #     for idx in range(len(s)):
    #         ingroupidx = idx % (2 * (numRows - 1))
    #         listid = ingroupidx if ingroupidx-numRows+1 <=0 else 2*numRows-ingroupidx-2
    #         res[listid] += s[idx]
    
    #     return ''.join(res)

    #   ✔ Accepted
    #       ✔ 1158/1158 cases passed (68 ms)
    #       ✔ Your runtime beats 68.49 % of python3 submissions
    #       ✔ Your memory usage beats 37.44 % of python3 submissions (13.3 MB)

        if numRows == 1 or numRows >= len(s):
            return s
        
        res, index, step = [''] * numRows, 0, 1
        for i in s:
            res[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        
        return ''.join(res)
        # ✔ Accepted
        #     ✔ 1158/1158 cases passed (56 ms)
        #     ✔ Your runtime beats 96.23 % of python3 submissions
        #     ✔ Your memory usage beats 27.5 % of python3 submissions (13.4 MB)

