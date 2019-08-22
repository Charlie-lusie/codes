n, m = list(map(int, input().split()))
graph = [[0 for i in range(n)] for j in range(n)]
while 1:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0: break
    graph[a][b] = 1
    graph[b][a] = 1
