class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0: return 0
        if len(numbers) < 2: return numbers[0]
        ddict = {}
        for n in numbers:
            if n in ddict.keys():
                ddict[n] = ddict[n] + 1
                if ddict[n] > float(len(numbers))/2.0:
                    return n
            else:
                ddict[n] = 0
        return 0

a = [1,2,3,2,2,2,5,4,2]
s = Solution()
b = s.MoreThanHalfNum_Solution(a)
print(b)