#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        self.solver(s, 0, '', res)
        return res

    def solver(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.solver(s[i:], index+1, path+s[:i]+'.', res)
                elif i == 2 and s[0] != '0':
                    self.solver(s[i:], index+1, path+s[:i]+'.', res)
                elif i == 3 and s[0] != '0' and int(s[:i]) < 256:
                    self.solver(s[i:], index+1, path+s[:i]+'.', res)
✔ Accepted
  ✔ 147/147 cases passed (36 ms)
  ✔ Your runtime beats 91.12 % of python3 submissions
  ✔ Your memory usage beats 5.56 % of python3 submissions (13.9 MB)      
        
# if __name__ == "__main__":
#     ip = "010010"
#     res = Solution().restoreIpAddresses(ip)


