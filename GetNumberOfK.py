# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0: return 0
        if k <data[0] or k > data[-1]: return 0
        first = self.GetFirst(data, k, 0, len(data)-1)
        last = self.GetLast(data, k, 0, len(data)-1)
        if (first > -1 and last > -1):
            return last - first + 1
        else:
            return 0
    def GetFirst(self, data, k, begin, end):
        if (begin > end): return -1
        pos = int((begin + end) / 2)
        elem = data[pos]
        if elem == k:
            if (pos >0 and data[pos-1] !=k) or pos == 0:
                return pos
            else:
                end = pos - 1
        elif elem > k:
            end = pos - 1
        else:
            begin = pos + 1
        return self.GetFirst(data, k, begin, end)
    
    def GetLast(self, data, k, begin, end):
        if begin > end: return -1
        pos = int((begin + end) / 2)
        elem = data[pos]
        if elem == k:
            if (pos < len(data) - 1 and data[pos+1] !=k) or pos == len(data) - 1:
                return pos
            else:
                begin = pos + 1
        elif elem < k:
            begin = pos + 1
        else:
            end = pos - 1
        return self.GetLast(data, k, begin, end)

A = Solution()
print(A.GetNumberOfK([1,2,3,4,4,4,5,6,6,6,7], 6))


