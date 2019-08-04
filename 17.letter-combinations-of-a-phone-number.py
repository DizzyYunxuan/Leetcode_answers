#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str):
        dic = {'2':'abc', '3':'def',
        '4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'}
        l = []
        if len(digits) == 0:
            return 
        if len(digits) == 1:
            return dic[digits[0]]
        prev = self.letterCombinations(digits[:-1])
        suc = dic[digits[-1]]
        for i in prev:
            for j in suc:
                l.append(i+j)
        return l
        
# ✔ Accepted
#   ✔ 25/25 cases passed (32 ms)
#   ✔ Your runtime beats 92.12 % of python3 submissions
#   ✔ Your memory usage beats 5.39 % of python3 submissions (13.9 MB)
# # if __name__ == '__main__':
#     res = Solution().letterCombinations('234')
#     print(res)
