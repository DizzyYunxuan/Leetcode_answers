#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#

# @lc code=start
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        prefixsum = [0]
        for n in nums:
            prefixsum.append(prefixsum[-1]+n)

        return self.mergeSort(0, len(prefixsum), prefixsum, lower, upper)


    def mergeSort(self, low, high, prefixsum, lower, upper):
        if high - low <= 1:
            return 0
        mid = (low + high) // 2
        count = self.mergeSort(low, mid, prefixsum, lower, upper) + self.mergeSort(mid, high, prefixsum, lower, upper)
        i = j = mid
        for left in prefixsum[low:mid]:
            while i < high and prefixsum[i] - left < lower: i += 1
            while j < high and prefixsum[j] - left <= upper: j += 1
            count += j - i
        prefixsum[low:high] = sorted(prefixsum[low:high])
        return count
Accepted
61/61 cases passed (228 ms)
Your runtime beats 65.9 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (14.4 MB)
# if __name__ == "__main__":
#     res = Solution().countRangeSum([-2,5,-1], -2, 2)

# @lc code=end

