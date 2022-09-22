import sys
sys.setrecursionlimit(10**8)
def dfs(i,j,h):
    visited[i][j] = 1
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    for n in range(len(di)):
        ni = i + di[n]
        nj = j + dj[n]
        if 0<= ni<N and 0<= nj <N and visited[ni][nj] == 0 and mat[ni][nj]>h:
            dfs(ni,nj,h)
    return 1
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
height = [0]
maxs= 0
for i in range(N):          # 높이 배열 만들기
    for j in range(N):
        height.append(mat[i][j])
height = set(height)
height = list(height)
for k in height:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] >k and visited[i][j] == 0:
                cnt += dfs(i,j,k)
    if maxs < cnt:
        maxs = cnt
print(maxs)
