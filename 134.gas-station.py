#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, restgas, allgas = 0, 0, 0
        for i in range(len(gas)):
            restgas += gas[i] - cost[i]
            allgas += gas[i] - cost[i]
            if restgas < 0:
                start, restgas = i + 1, 0
        return start if allgas >= 0 else -1
✔ Accepted
  ✔ 31/31 cases passed (64 ms)
  ✔ Your runtime beats 60.93 % of python3 submissions
  ✔ Your memory usage beats 6.25 % of python3 submissions (14.8 MB)
