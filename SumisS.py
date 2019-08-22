import math
class Solution:
    def FindContinuousSequence(self, tsum):#找连续正数的和为S的所有子列
        # write code here
        if tsum <= 2: return []
        result = []
        for i in range(2, int(math.sqrt(2*tsum))+1):
            if (i % 2 != 0 and tsum % i == 0) or (tsum % i)*2 == i:
                a1 = int((2*tsum + i - i**2)/(2*i))
                result.append([_i for _i in range(a1, a1+i)])
        return result[::-1]
    def FindNumbersWithSum(self, array, tsum):#从有序数列里面找两个数字的和为S，若存在多组，返回乘积最小的一组
        if len(array) < 2: return []
        if array[0]+array[-1] < tsum: return []
        result = []
        times = []
        low, high = 0, len(array)-1
        while(low < high):
            s = array[low] + array[high]
            if s < tsum:
                low += 1
            elif s > tsum:
                high -= 1
            else:
                result.append([array[low], array[high]])
                times.append(array[low]*array[high])
                low += 1
                high -= 1
        if len(times) == 0: return []
        idx = times.index(min(times))
        Result = result[idx]
        return Result


A = Solution()
print(A.FindContinuousSequence(100))
print(A.FindNumbersWithSum([1,2,4,7,11,15], 15))