#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length = len(num)
        if length <= 2:
            return False
        
        for firstend in range(1, len(num)):
            for secondend in range(firstend+1, len(num)):
                first, second = num[:firstend], num[firstend:secondend]
                if len(str(int(first) + int(second))) > length - secondend \
                    or (len(second) > 1 and second[0] == '0') \
                    or (len(first) > 1 and first[0] == '0'):
                    break
                if self.isOK(first, second, num[secondend:]):
                    return True
        return False

    def isOK(self, pre, cur, num):
        if not num:
            return True
        cursum = str(int(pre) + int(cur))
        if num[:len(cursum)] == cursum:
            return self.isOK(cur, cursum, num[len(cursum):])
        else:
            return False
Accepted
41/41 cases passed (36 ms)
Your runtime beats 75.81 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (13.9 MB)                
# if __name__ == "__main__":
#     res = Solution().isAdditiveNumber("1023")






# @lc code=end

