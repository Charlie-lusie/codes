class Solution:
    def Subset(self, s):
        ans, path = [], []
        ans.append(path)
        s.sort()
        for i in range(1, len(s)+1):
            path = []
            self.DFS(s, ans, path, 0, 0, i)
        return ans
    def DFS(self, s, ans, path, start, count, max_count):
        if count == max_count:
            ans.append(path[:])
            return
        for j in range(start, len(s)):
            path.append(s[j])
            self.DFS(s, ans, path, j + 1, count + 1, max_count)
            path.pop()

A = Solution()
print(A.Subset([1,2,3]))