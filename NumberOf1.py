# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if (n<=0): return 0
        k = 10
        digits = []
        while(abs(n) >= 1e-5):
            m = n%k
            n = int(n/k)
            digits.append(m)
        return self.Count1(digits)
    def Count1(self, digit):
        if (len(digit) == 0): return 0
        L, first = len(digit), digit[-1]
        if (L == 1):
            if (first <= 0): return 0
            elif(first > 0): return 1
        
        number_of_first_digit = 0
        if (first > 1):
            number_of_first_digit = self.FindNumberOfOneDigit(L - 1)
        elif (first == 1):
            number_of_first_digit = self.DigitsToNumber(digit[0:L - 1]) + 1
        number_of_other_digit = first*(L - 1)*self.FindNumberOfOneDigit(L - 2)
        number_of_last_digit = self.Count1(digit[0:L - 1])

        return number_of_first_digit + number_of_other_digit + number_of_last_digit
    def FindNumberOfOneDigit(self, L):
        return 10**L
    def DigitsToNumber(self, di):
        L = len(di)
        return sum([di[x]*10**x for x in range(0, L)])

A = Solution()
b = A.NumberOf1Between1AndN_Solution(10)
print(b)