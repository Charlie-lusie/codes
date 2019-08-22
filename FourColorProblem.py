#  给定无向连通图G=(V, E)和m种不同的颜色，用这些颜色为图G的各顶点着色，每个顶点着一种颜色。是否有一种着色法使G中相邻的两个顶点有不同的颜色?
#         这个问题是图的m可着色判定问题。若一个图最少需要m种颜色才能使图中每条边连接的两个顶点着不同颜色，则称这个数m为该图的色数。求一个图的色数m的问题称为图的m可着色优化问题。
#         编程计算：给定图G=(V, E)和m种不同的颜色，找出所有不同的着色法和着色总数
# 输入
# 第一行是顶点的个数n（2≤n≤10），颜色数m（1≤m≤n）。接下来是顶点之间的相互关系：a b,表示a和b相邻。当a，b同时为0时表示输入结束, so a&b count from 1
# 输出
# 输出所有的着色方案，表示某个顶点涂某种颜色号，每个数字的后面有一个空格。最后一行是着色方案总数。
count = 0

def ThisColorCanBeUse(cur, color, n):
    for i in range(n):
        if graph[cur][i+1] and color[cur] == color[i+1]:#与cur相连的所有节点都不能与之同色
            return False
    return True

def FindColorSheme(cur, color, n, m):
    global count
    if (cur > n):#所有节点都已经遍历完, 这就是一种新的涂色方法
        # for i in range(n):
            #print(color[i+1], end = ' ')
        count += 1
        #print('\n')
    else:
        for i in range(m):#对当前节点cur，遍历所有颜色找可用的
            color[cur] = i + 1
            if ThisColorCanBeUse(cur, color, n):
                FindColorSheme(cur + 1, color, n, m)#回溯到上一层.从这里出来说明一个涂色方法已经找到，这时候将当前节点的颜色值重置(color[cur] =0)，继续遍历，前面的节点保持不变
            color[cur] = 0

n, m = list(map(int, input().split()))
graph = [[0 for i in range(n + 1)] for j in range(n + 1)]
color = [0 for i in range(n + 1)]
while 1:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0: break
    graph[a][b] = 1
    graph[b][a] = 1
FindColorSheme(1, color, n, m)
print("Total count = ", count)