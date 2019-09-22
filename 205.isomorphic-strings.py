#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
✔ Accepted
  ✔ 30/30 cases passed (40 ms)
  ✔ Your runtime beats 92.65 % of python3 submissions
  ✔ Your memory usage beats 17.5 % of python3 submissions (14 MB)


#     def isIsomorphic(self, s: str, t: str) -> bool:
#         d1, d2 = {}, {}
#         for i, val in enumerate(s):
#             d1[val] = d1.get(val, []) + [i]
#         for i, val in enumerate(t):
#             d2[val] = d2.get(val, []) + [i]
#         return sorted(d1.values()) == sorted(d2.values())
# ✔ Accepted
#   ✔ 30/30 cases passed (160 ms)
#   ✔ Your runtime beats 5.93 % of python3 submissions
#   ✔ Your memory usage beats 5 % of python3 submissions (16.6 MB)



    # def isIsomorphic(self, s: str, t: str) -> bool:
        # d1, d2 = {}, {}
        # i, cur1, cur2 = 0, '`', '`'
        # while i < len(s):
        #     if s[i] not in d1:
        #         cur1 = chr(ord(cur1)+1)
        #         d1[s[i]] = cur1
        #         s = s[:i]+cur1+s[i+1:]
        #     else:
        #         s = s[:i]+d1[s[i]]+s[i+1:]                    
        #     if t[i] not in d2:
        #         cur2 = chr(ord(cur2)+1)
        #         d2[t[i]] = cur2
        #         t = t[:i]+cur2+t[i+1:]
        #     else:

        #         t = t[:i]+d2[t[i]]+t[i+1:]                
        #     i += 1
        # return s == t
# ✔ Accepted
#   ✔ 30/30 cases passed (392 ms)
#   ✔ Your runtime beats 5.67 % of python3 submissions
#   ✔ Your memory usage beats 17.5 % of python3 submissions (13.9 MB)



# if __name__ == "__main__":
#     res = Solution().isIsomorphic('egg', 'add')
