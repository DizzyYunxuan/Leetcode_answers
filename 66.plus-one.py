#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        i = len(digits) - 1
        carry = 0
        while i > -1:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1
        if carry:
            digits.insert(0, 1)
        return digits
✔ Accepted
  ✔ 109/109 cases passed (40 ms)
  ✔ Your runtime beats 59.85 % of python3 submissions
  ✔ Your memory usage beats 5.13 % of python3 submissions (14 MB)
    
# if __name__ == "__main__":
#     res = Solution().plusOne([9,9])
