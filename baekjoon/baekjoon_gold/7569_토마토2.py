from collections import deque
def bfs():
    for i in range(size):
        for j in range(M):
            if tomatos[i][j] == 1:
                Q.append((i,j))
                visited[i][j] = 1
            if tomatos[i][j] == -1:
                visited[i][j] = -1
    dx = [1,-1,0,0,N,-N]
    dy = [0,0,1,-1,0,0]
    while Q:
        i,j = Q.popleft()
        for k in range(len(dx)):
            if i%N == 0 and k==1 and i>0:
                continue
            if (i+1)%N ==0 and k==0 and i>=N-1:
                continue
            ni,nj = i+dx[k],j+dy[k]
            if 0 <= ni < size and 0 <= nj < M and tomatos[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                Q.append((ni, nj))

M,N,H = map(int,input().split())
size = N*H
tomatos = [list(map(int,input().split())) for _ in range(size)]
Q = deque([])
visited = [[0]*M for _ in range(size)]
bfs()
cnt = 0
maxs = 0
for i in range(size):
    for j in range(M):
        if visited[i][j]==0:
            cnt = -1
            break
        if maxs < visited[i][j]:
            maxs = visited[i][j]
    if cnt == -1:
        break
if cnt == -1:
    print(-1)
else:
    print(maxs-1)

