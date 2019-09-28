#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        sp = self.splitNum(num)
        case = ['', 'Thousand', 'Million', 'Billion']
        place1 = ['', 'One', 'Two', 'Three',\
            'Four', 'Five', 'Six', 'Seven',\
                    'Eight', 'Nine']
        place2 = ['', 'Ten', 'Twenty', 'Thirty',\
                    'Forty', 'Fifty', 'Sixty', 'Seventy',\
                    'Eighty', 'Ninety', 'Ten', 'Eleven',\
                    'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        res = ''   
        for i in range(len(sp)):       
            if sp[i]:
                res  = ' ' + self.num2word(sp[i], place1, place2) + ' ' + case[i] + res
        return res.strip()

    def splitNum(self, num):
        sp = []
        while num != 0:
            sp.append(num % 1000)
            num //= 1000
        return sp

    def num2word(self, num, place1, place2):
        p1, p2 = num // 100, num % 100
        s = place1[p1] + ' ' + 'Hundred ' if p1 else ''

        if p2 >= 20:
            s += place2[p2//10] + ' ' + place1[p2%10]
        elif 10 <= p2 < 20:
            s += place2[p2]
        else:
            s += place1[p2]
        return s.strip()
✔ Accepted
  ✔ 601/601 cases passed (36 ms)
  ✔ Your runtime beats 87.2 % of python3 submissions
  ✔ Your memory usage beats 8.7 % of python3 submissions (13.9 MB)
# if __name__ == "__main__":
#     res = Solution().numberToWords(50868)


