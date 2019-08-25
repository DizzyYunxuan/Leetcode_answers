#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = self.bbsort(candidates)
        # candidates.sort()
        res = []
        self.allSum(candidates, target, [], res, 0)
        return res
    
    def allSum(self, candidates, target, track, res, index):
        if target < 0:
            return
        if target == 0:
            res.append(track)
            return 
        for i in range(index, len(candidates)):
            self.allSum(candidates, target - candidates[i], track+[candidates[i]], res, i)

    def bbsort(self, candidates):
        for tail in range(len(candidates)):
            i = len(candidates) - 1
            while i > tail:
                if candidates[i] < candidates[i-1]:
                    candidates[i], candidates[i-1] = candidates[i-1], candidates[i]
                i -= 1
        return candidates

✔ Accepted
  ✔ 168/168 cases passed (120 ms)
  ✔ Your runtime beats 30.39 % of python3 submissions
  ✔ Your memory usage beats 6.06 % of python3 submissions (13.8 MB)


