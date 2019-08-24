# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s) == 0: return ''
        words = []
        p1, p2 = 0, 0
        while(p2 < len(s)):
            if p2 == len(s) - 1:
                words.append(s[p1:p2 + 1])
                p2 += 1
                p1 = 1*p2
            elif s[p2] == ' ':
                words.append(' ' + s[p1:p2])
                p2 += 1
                p1 = 1*p2
            else:
                p2 += 1
        if len(words) == 0:return ''
        result = []
        for i in range(len(words)-1, -1, -1):
            result.append(words[i])
        return ('').join(result)
    def ReverseSentence2(self, s):
        if len(s) == 0: return ''
        words = s.split()
        if len(words) == 0: return s
        result = []
        for i in range(len(words)-1, -1, -1):
            result.append(words[i])
        return ('').join(result)
    def ReverseSentence3(self, s):
        ss =  " ".join(s.split()[::-1]) if s.strip() != "" else s
        return ss

A = Solution()
print(A.ReverseSentence3(" "))

