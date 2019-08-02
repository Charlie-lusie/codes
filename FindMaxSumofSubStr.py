class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, current_sum = float('-inf'), 0
        for i in array:
            if (current_sum <= 0):
                current_sum = i
            else:
                current_sum += i
            if (current_sum > max_sum):
                max_sum = current_sum
        return max_sum

A = Solution()
b = A.FindGreatestSumOfSubArray([-2, -8, -1, -5, -9])
print(b)