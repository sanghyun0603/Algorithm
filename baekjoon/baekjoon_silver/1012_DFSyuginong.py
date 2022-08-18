import sys
sys.setrecursionlimit(10000)
def dfs(i,j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[i][j] = 1
    for k in range(len(dx)):
        di = i + dy[k]
        dj = j + dx[k]
        if (0<= di < N) and (0<= dj < M):
            if visited[di][dj] == 0 and mat[di][dj] == 1:
                dfs(di,dj)


T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    mat = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x,y = map(int,input().split())
        mat[y][x] = 1
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and mat[i][j] == 1:
                dfs(i,j)
                cnt +=1
    print(cnt)