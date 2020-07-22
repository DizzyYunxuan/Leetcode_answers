#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if not input: return 0
        print(input)
        # tree = self.construct_tree(input)
        # print(input.split(r'\n'))

    def construct_tree(self, s):
        tree, name, cur_path, i = {}, '', [], 0
        while i < len(s):
            if s[i] == 'n' and s[i-1] == '\\':
                if '.' in name:
                    
                    
                cur_path.append(name[:-1])
                j, count = i
                while s[j] != 'n' and s[j-1] != '\\':


            
            name += s[i]
            i += 1
                     
                
                
            
                





# @lc code=end

