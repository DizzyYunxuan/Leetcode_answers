#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
class Solution:
    def solve(self, idx, i):
        if idx == 3:
            return i * 'M'    
        elif idx == 2:
            if i == 9:
                return 'CM'  
            elif i > 5 and i < 9:
                return  'D' + (i - 5) * 'C'
            elif i == 5:
                return  'D'   
            elif i == 4:
                return 'CD'  
            else:
                return i * 'C'  
        elif idx == 1:
            if i == 9:
                return 'XC'  
            elif i > 5 and i < 9:
                return  'L' + (i - 5) * 'X'
            elif i == 5:
                return  'L'   
            elif i == 4:
                return 'XL'  
            else:
                return i * 'X'  
        else:
            if i == 9:
                return 'IX'  
            elif i > 5 and i < 9:
                return  'V' + (i - 5) * 'I'
            elif i == 5:
                return  'V'   
            elif i == 4:
                return 'IV'  
            else:
                return i * 'I' 
            
    def intToRoman(self, num: int) -> str:
        res, nums = '', []
        for i in str(num):
            nums.insert(0, int(i))
        for i in range(len(nums)):
            res = self.solve(i, nums[i])+ res
        return res
    
#     ✔ Accepted
#   ✔ 3999/3999 cases passed (60 ms)
#   ✔ Your runtime beats 50.77 % of python3 submissions
#   ✔ Your memory usage beats 5.08 % of python3 submissions (14.1 MB)
    
    # def intToRoman(self, num: int) -> str:
    #     M = ["", "M", "MM", "MMM"]
    #     C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    #     X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    #     I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    #     return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]
#     ✔ Accepted
#   ✔ 3999/3999 cases passed (56 ms)
#   ✔ Your runtime beats 70.32 % of python3 submissions
#   ✔ Your memory usage beats 5.08 % of python3 submissions (13.9 MB)
