#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
✔ Accepted
  ✔ 101/101 cases passed (112 ms)
  ✔ Your runtime beats 79.49 % of python3 submissions
  ✔ Your memory usage beats 30.19 % of python3 submissions (17.4 MB)
# if __name__ == "__main__":
#     res = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # res = Solution().groupAnagrams(["","",""])
