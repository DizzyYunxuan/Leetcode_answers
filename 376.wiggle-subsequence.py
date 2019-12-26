#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) < 2: return len(nums)
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)

Accepted
27/27 cases passed (32 ms)
Your runtime beats 86.76 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.8 MB)






    # def wiggleMaxLength(self, nums) -> int:
    #     if len(nums) < 2: return len(nums)
    #     return max(1 + self.calculate(nums, 0, True), 1 + self.calculate(nums, 0, False))
    
    # def calculate(self, nums, start, isUp):
    #     maxlen = 0
    #     for i in range(start+1, len(nums)):
    #         if (isUp and nums[i] > nums[start]) or (not isUp and nums[i] < nums[start]):
    #             maxlen = max(maxlen, 1 + self.calculate(nums, i, not isUp)) 
    #     return maxlen
    # Time Limit Exceeded



# if __name__ == "__main__":
#     res = Solution().wiggleMaxLength([1,7,4,9,2,5])   
            

# @lc code=end

