#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return 0
        m = max(nums)
        bucks = [[] for _ in range(10)]
        loops = 1
        while m // loops != 0:
            bucks = [[] for _ in range(10)]
            for i in nums:
                bucks[(i // loops) % 10].append(i)
            nums = bucks[0]
            for j in bucks[1:]:
                nums += j
            loops *= 10
        res = 0
        for i in range(n-1):
            res = max(nums[i+1]-nums[i], res)
        return res
# ✔ Accepted
#   ✔ 18/18 cases passed (76 ms)
#   ✔ Your runtime beats 44.09 % of python3 submissions
#   ✔ Your memory usage beats 33.33 % of python3 submissions (14.8 MB)
# if __name__ == "__main__":
#     a = [1, 1000]
#     res = Solution().maximumGap(a)

