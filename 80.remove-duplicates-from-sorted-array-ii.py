#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return
        wait_for_delete, cur, count = [], nums[0], 0
        for i in range(len(nums)):
            if nums[i] == cur:
                count += 1
                if count > 2:
                    wait_for_delete.append(nums[i])
            else: 
                cur = nums[i]
                count = 1
        for i in wait_for_delete:
            nums.remove(i)
        return len(nums)
# if __name__ == "__main__":
#     a = [0,0,1,1,1,1,2,3,3]
#     res = Solution().removeDuplicates(a)
