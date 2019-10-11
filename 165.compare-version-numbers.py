#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1, s2 = version1.split('.'), version2.split('.')
        length = max(len(s1), len(s2))
        s1, s2 = s1 + ['0']*(length - len(s1)), s2 + ['0']*(length - len(s2))
        for i in range(length):
            if int(s1[i]) > int(s2[i]):
                return 1
            elif int(s1[i]) < int(s2[i]):
                return -1
        return 0
# ✔ Accepted
#   ✔ 72/72 cases passed (36 ms)
#   ✔ Your runtime beats 70.01 % of python3 submissions
#   ✔ Your memory usage beats 8.33 % of python3 submissions (13.8 MB)

if __name__ == "__main__":
    version1, version2 = '0.1', '1.1'
    res = Solution().compareVersion(version1, version2)
    print(res)
