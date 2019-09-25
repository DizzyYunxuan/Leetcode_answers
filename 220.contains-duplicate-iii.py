#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False
        all_buckets = {}
        for i in range(len(nums)):
            bucket_idx = nums[i] // (t + 1)
            if bucket_idx in all_buckets:
                return True
            all_buckets[bucket_idx] = nums[i]
            if bucket_idx-1 in all_buckets and abs(all_buckets[bucket_idx-1]-nums[i]) <= t:
                 return True
            if bucket_idx+1 in all_buckets and abs(all_buckets[bucket_idx+1]-nums[i]) <= t:
                 return True   
            if i >= k:
                all_buckets.pop(nums[i-k]//(t+1))
        return False
✔ Accepted
  ✔ 41/41 cases passed (72 ms)
  ✔ Your runtime beats 60 % of python3 submissions
  ✔ Your memory usage beats 33.33 % of python3 submissions (15.9 MB)        

# if __name__ == '__main__':
#     Solution().containsNearbyAlmostDuplicate([3,6,0,4], 2, 2)
