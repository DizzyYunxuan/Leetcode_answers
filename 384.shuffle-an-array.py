#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start
from itertools import permutations
import random
class Solution:

    def __init__(self, nums):
        self.arr = nums.copy()
        self.shuffle_arr = nums.copy()
        
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffle_arr = self.arr.copy()
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        res = []
        while self.shuffle_arr:
            index = random.randint(0, len(self.shuffle_arr)-1)
            self.shuffle_arr[-1], self.shuffle_arr[index] = self.shuffle_arr[index], self.shuffle_arr[-1]
            res.append(self.shuffle_arr.pop())
        self.shuffle_arr = res.copy()
        return self.shuffle_arr


# Your Solution object will be instantiated and called as such:
# nums = [1,2,3]
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# print(param_2)
# print()
# @lc code=end

Accepted
10/10 cases passed (380 ms)
Your runtime beats 31.19 % of python3 submissions
Your memory usage beats 88.66 % of python3 submissions (18.9 MB)