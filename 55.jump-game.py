#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
class Solution:
    def canJump(self, nums) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
# if __name__ == "__main__":
#     res = Solution().canJump([2,3,1,1,4])
#     print(res)
