# -*- coding:utf-8 -*-
class Solution:
    result = []
    temp = []
    def Permutation(self, ss):
        # write code here
        if len(ss) == 0: return self.result
        single = list(ss)
        single.sort()
        self.FindAll(single)
        self.result = list(set(self.result))
        self.result.sort()
        return self.result
    def FindAll(self, s):
        if len(s) == 1:
            self.temp.append(s[0])
            self.result.append("".join(self.temp))
            self.temp.pop()
            return
        for k, v in enumerate(s):
            self.temp.append(v)
            self.FindAll(s[:k] + s[k+1:])
            self.temp.pop()
        return

A = Solution()
b = A.Permutation('aa')
print(b)