# -*- coding:utf-8 -*-
import random
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        result = []
        if (len(tinput) == 0 or k <= 0 or k > len(tinput)): return result
        pos, start, end = -1, 0, len(tinput) - 1
        while(pos != k - 1):
            if (pos > k - 1): end = pos - 1
            else: start = pos + 1
            pos, tinput = self.exchange(tinput, start, end)
        return tinput[0:k]
    
    def exchange(self, input, st, en):
        pos = st
        pick_one_element = random.randint(st, en)
        input[pick_one_element], input[en] = input[en], input[pick_one_element]# pick one and put it to the end
        for i in range(st, en):
            if (input[i] <= input[en]):
                if (pos != i): 
                    input[pos], input[i] = input[i], input[pos]#exchange numbers
                pos += 1
        input[pos], input[en] = input[en], input[pos]
        return pos, input



A = Solution()
b = A.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4)
print(b)