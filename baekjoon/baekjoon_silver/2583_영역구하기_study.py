import sys
sys.setrecursionlimit(10**8)
def dfs(i,j):
    global cnt
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    visited[i][j] = 1
    cnt += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<= ni < M and 0<= nj < N and visited[ni][nj] == 0 and mat[ni][nj] == 0:
            dfs(ni,nj)


M,N,K = map(int,input().split())
mat = [[0]*N for _ in range(M)]
cnt = 0
cnt_li = []
for _ in range(K):
    c1,r1,c2,r2 = map(int,input().split())
    for i in range(r1,r2):
        for j in range(c1,c2):
            mat[i][j] = 1
visited = [[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if mat[i][j] == 0 and visited[i][j] == 0:
            dfs(i,j)
            cnt_li.append(cnt)
            cnt = 0
cnt_li.sort()
print(len(cnt_li))
print(*cnt_li)