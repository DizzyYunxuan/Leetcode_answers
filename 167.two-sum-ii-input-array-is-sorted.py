#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:
    def twoSum(self, numbers, target: int):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
✔ Accepted
✔ 17/17 cases passed (76 ms)
✔ Your runtime beats 60.3 % of python3 submissions
✔ Your memory usage beats 5.8 % of python3 submissions (14.2 MB)  
# if __name__ == "__main__":
#     num, target = [-1,0], -1
#     res = Solution().twoSum(num, target)

