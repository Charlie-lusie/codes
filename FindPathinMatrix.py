class Solution:
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    border = []
    def hasPath(self, matrix, rows, cols, path):
        if rows <= 0 or cols <= 0: return False
        if len(path) == 0: return False
        m1 = [[1 for i in range(cols)] for j in range(rows)]
        k = 0
        for i in range(rows):
            for j in range(cols):
                m1[i][j] = matrix[k]
                k += 1
        m2 = [[0 for i in range(cols)] for j in range(rows)]
        start = []
        for i in range(rows):
            for j in range(cols):
                if m1[i][j] == path[0]:
                    start.append([i, j])
        for i in range(len(start)):
            m2[start[i][0]][start[i][1]] = -1 #visited
            if self.FindPath(1*start[i], m1, 1*m2, path[1:]): return True#up
            m2[start[i][0]][start[i][1]] = 0
        return False
    def FindPath(self, pos, m, m2, path):
        if len(path) == 0: return True
        if pos[0] > 0 and m2[pos[0] - 1][pos[1]] != -1 and m[pos[0] - 1][pos[1]] == path[0]:#up
            pos[0] -= 1 #move one step
            m2[pos[0]][pos[1]] = -1
            if self.FindPath(1*pos, m, 1*m2, path[1:]): return True
            m2[pos[0]][pos[1]] = 0
            pos[0] += 1 #move one step
        if pos[1] > 0 and m2[pos[0]][pos[1] - 1] != -1 and m[pos[0]][pos[1] - 1] == path[0]:#left
            pos[1] -= 1
            m2[pos[0]][pos[1]] = -1
            if self.FindPath(1*pos, m, 1*m2, path[1:]): return True
            m2[pos[0]][pos[1]] = 0
            pos[1] += 1
        if pos[0] < len(m) - 1 and m2[pos[0] + 1][pos[1]] != -1 and m[pos[0] + 1][pos[1]] == path[0]:
            pos[0] += 1
            m2[pos[0]][pos[1]] = -1
            if self.FindPath(1*pos, m, 1*m2, path[1:]): return True
            m2[pos[0]][pos[1]] = 0
            pos[0] -= 1
        if pos[1] < len(m[0]) - 1 and m2[pos[0]][pos[1] + 1] != -1 and m[pos[0]][pos[1] + 1] == path[0]:
            pos[1] += 1
            m2[pos[0]][pos[1]] = -1
            if self.FindPath(1*pos, m, 1*m2, path[1:]): return True
            m2[pos[0]][pos[1]] = 0
            pos[1] -= 1
        return False
    def hasPath2(self, matrix, rows, cols, path):
        if rows <= 0 or cols <= 0: return False
        if len(path) == 0: return False
        m2 = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if Judge(matrix, i, j, rows, cols, m2)

A = Solution()
print(A.hasPath('ABCESFCSADEE', 3, 4, 'SEE'))
        


