#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) < 1: return len(nums)
        res = 0
        for start in range(len(nums)):
            sq = nums[start]
            aOrd, l = True, 1
            for j in range(start+1, len(nums)):
                if l < 2 and nums[j] != sq:
                    if nums[j] - sq < 0:
                        aOrd = True
                    elif nums[j] - sq > 0:
                        aOrd = False
                    sq = nums[j]
                    l += 1
                    continue

                if nums[j] - sq > 0 and aOrd:
                    sq = nums[j]
                    aOrd = False
                    l += 1
                elif nums[j] - sq < 0 and not aOrd:
                    sq = nums[j]
                    aOrd = True
                    l += 1
            res = max(res, l)
        return res

if __name__ == "__main__":
    res = Solution().wiggleMaxLength([1,7,4,9,2,5])   
            

# @lc code=end

