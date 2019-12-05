#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes: return 0
        envelopes = sorted(envelopes, key=lambda x: [x[0], -x[1]])
        nums = [i[1] for i in envelopes]

        return self.LongestIncreasingSeries(nums)

    def LongestIncreasingSeries(self, nums):
        top = [0] * len(nums)
        piles = 0
        for n in nums:
            low, high = 0, piles
            while low < high:
                mid = (low + high) // 2
                if top[mid] > n:
                    high = mid
                elif top[mid] < n:
                    low = mid + 1
                else:
                    high = mid
            if low == piles:
                piles += 1
            top[low] = n
        return piles
Accepted
85/85 cases passed (172 ms)
Your runtime beats 84.31 % of python3 submissions
Your memory usage beats 20 % of python3 submissions (15 MB)

# if __name__ == "__main__":
#     envelopes = [[5,4],[6,4],[6,7],[2,3]]
#     res = Solution().maxEnvelopes(envelopes)
#     print(res)
    
# @lc code=end

