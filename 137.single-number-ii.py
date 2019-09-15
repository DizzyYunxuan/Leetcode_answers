#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
class Solution:
    def singleNumber(self, nums) -> int:
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num # 二进制某位出现1次时twos = 0，出现2, 3次时twos = 1；
            ones ^= num  # 二进制某位出现2次时ones = 0，出现1, 3次时ones = 1；
            threes = ones & twos # 二进制某位出现3次时（即twos = ones = 1时）three = 1，其余即出现1, 2次时three = 0；
            ones &= ~threes # 将二进制下出现3次的位置零，实现`三进制下不考虑进位的加法`；
            twos &= ~threes
        return ones

if __name__ == "__main__":
    res = Solution().singleNumber([2,2,3,2])

#   def singleNumber(self, nums: List[int]) -> int:
#         return (3 * sum(set(nums)) - sum(nums))//2
# ✔ Accepted
#   ✔ 11/11 cases passed (68 ms)
#   ✔ Your runtime beats 71.95 % of python3 submissions
#   ✔ Your memory usage beats 6.67 % of python3 submissions (15.6 MB)
