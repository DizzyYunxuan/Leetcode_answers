#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            count = 0
            for j in range(i+1, len(nums)):
                if nums[j] < cur:
                    count += 1
            res.append(count)
        return res

# @lc code=end

