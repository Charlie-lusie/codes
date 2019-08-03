class Solution:

    def InversePairs(self, L1):
        if (len(L1) == 0): return 0
        L2 =1*L1#for deep copy
        return self.InversePairsCore(L1, L2, 0, len(L1) - 1)

    def InversePairsCore(self, data, copy, start, end):
        if (start == end):
            copy[start] = data[start]
            return 0
        length = int((end - start) / 2)
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)
        i = start + length
        j = end
        index_copy = end
        count = 0
        while(i >= start and j >= start + length + 1):
            if (data[i] > data[j]):
                copy[index_copy] = data[i]
                index_copy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[index_copy] = data[j]
                index_copy -= 1
                j -= 1
        while(i >= start):
            copy[index_copy] = data[i]
            index_copy -= 1
            i -= 1
        while(j > start + length + 1):
            copy[index_copy] = data[j]
            index_copy -= 1
            j -= 1
        return left + right + count
    

A = Solution()
L2 = A.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575])
print(L2)