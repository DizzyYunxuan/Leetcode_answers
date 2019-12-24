#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums: return
        nums.sort()
        buckets = {}
        for num in nums:
            t = [num]
            for k in buckets:
                if num % k == 0 and len(buckets[k])+1 > len(t):
                    t = buckets[k] + [num]
            buckets[num] = t
        return max(buckets.values(), key=len)

Accepted
41/41 cases passed (300 ms)
Your runtime beats 97.5 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (12.9 MB)




# if __name__ == "__main__":
#     a = [4,8,3,6,12,1,2]
#     res = Solution().largestDivisibleSubset(a)


# @lc code=end

