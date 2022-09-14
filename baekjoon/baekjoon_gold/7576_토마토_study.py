from collections import deque

def bfs():
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1:
                Q.append((i,j))
                visited[i][j] = 1
            if tomatos[i][j] == -1:
                visited[i][j] = -1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while Q:
        i,j = Q.popleft()
        for k in range(len(dx)):
            ni,nj = i+dx[k],j+dy[k]
            if 0<= ni < N and 0<= nj < M and tomatos[ni][nj] ==0 and visited[ni][nj]==0:
                visited[ni][nj] = visited[i][j] + 1
                Q.append((ni,nj))



M , N = map(int,input().split())
tomatos = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
Q = deque([])
bfs()
maxs = 0
for i in range(N):          # 걸리는 요일수 찾기.
    for j in range(M):
        if visited[i][j] == 0:
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