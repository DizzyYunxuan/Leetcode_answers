#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
# #

class Solution:
    def findSubstring(self, s: str, words):

        if len(words) == 0:
            return []
        # initialize d, l, ans
        l = len(words[0])
        d = {}
        for w in words:# All words dict
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []
        # sliding window(s)
        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        # if the number of tword is larger than words_dict
                        # find the tword that is useless, 
                        # and all the words before the useless twords is also useless
                        # remove all useless words untill the number of twords == words_dict
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0
        return ans



# if __name__ == '__main__':
    # res = Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
    # res = Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])
    # res = Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
    # res = Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
    # res = Solution().findSubstring("abaababbaba", ["ba","ab","ab"])
    # print(res)


