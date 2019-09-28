#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
✔ Accepted
  ✔ 1012/1012 cases passed (44 ms)
  ✔ Your runtime beats 19.26 % of python3 submissions
  ✔ Your memory usage beats 6.67 % of python3 submissions (13.9 MB)

    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        while num != 1:
            if num % 2 and num % 3 and num % 5:
                return False
            else:
                if num % 2 == 0:
                    num //= 2
                elif num % 3 == 0:
                    num //= 3
                elif num % 5 == 0:
                    num //= 5
        return True
✔ Accepted
  ✔ 1012/1012 cases passed (40 ms)
  ✔ Your runtime beats 55.54 % of python3 submissions
  ✔ Your memory usage beats 6.67 % of python3 submissions (13.8 MB)       
                
# if __name__ == "__main__":
#     res = Solution().isUgly(8)
