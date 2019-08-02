class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0: return -1
        if len(s) == 1: return s[0]
        dd, idx = {}, {}
        for i, v in enumerate(s):
            if v in dd:
                dd[v] += 1
            else:
                dd[v] = 1
            idx[v] = i
        pos = len(s)
        for key, values in dd.items():
            if values == 1:
                pos = min(pos, idx[key])
        if pos == len(s):
            return -1
        else:
            return pos

A = Solution()
b = A.FirstNotRepeatingChar('google')
print(b)