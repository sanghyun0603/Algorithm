import sys
sys.setrecursionlimit(10000)

def dfs(i,j,color):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[i][j] = 1
    for k in range(4):
        dj = j + dx[k]
        di = i + dy[k]
        if (0 <= dj < N) and (0 <= di < N):
            if visited[di][dj] == 0 and mat[di][dj] == color:
                dfs(di,dj,col)

N = int(input())
mat = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
cnt_red = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mat[i][j] == 'R':
            col = 'R'
            dfs(i,j,col)
            cnt += 1
        elif visited[i][j] == 0 and mat[i][j] == 'G':
            col = 'G'
            dfs(i,j,col)
            cnt += 1
        elif visited[i][j] == 0 and mat[i][j] == 'B':
            col = 'B'
            dfs(i,j,col)
            cnt += 1
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'G':
            mat[i][j] = 'R'
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mat[i][j] == 'R':
            col = 'R'
            dfs(i,j,col)
            cnt_red += 1
        elif visited[i][j] == 0 and mat[i][j] == 'B':
            col = 'B'
            dfs(i,j,col)
            cnt_red += 1
print(cnt,cnt_red)