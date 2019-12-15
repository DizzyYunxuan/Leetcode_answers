#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        buckets, length = [], []
        for i in nums:
            if not buckets: 
                buckets.append([i])
                length.append(1)
                continue
            isEnter, longestIndex = False, 0
            for b in range(len(buckets)):
                if i % buckets[b][-1] == 0:
                    buckets[b].append(i)
                    isEnter = True
                else:
                    longestIndex = max(length[b], longestIndex)
            if not isEnter: 
                buckets.append(buckets[longestIndex][:-1]+[i])
                length.append(length[longestIndex]+1)
        
        index = length.index(max(length))
        return buckets[index]
            
if __name__ == "__main__":
    a = [4,8,3,6,12,1,2]
    res = Solution().largestDivisibleSubset(a)


# @lc code=end

