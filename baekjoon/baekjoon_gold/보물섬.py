from collections import deque
def bfs(i,j):
    cnt = 0
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    Q = deque([])
    Q.append([i,j])
    while Q:
        cnt += 1
        for i in range(len(Q)):
            qi,qj = Q.popleft()
            for k in range(len(di)):
                ni = qi + di[k]
                nj = qj + dj[k]
                if 0<= ni<N and 0<= nj <M and visited[ni][nj] ==0 and mat[ni][nj] =='L':
                    visited[ni][nj] = 1
                    Q.append([ni,nj])
    return cnt
N , M = map(int,input().split())
mat = [list(input()) for _ in range(N)]
maxs = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'L':
            s =bfs(i,j)
            if maxs<s:
                maxs = s
print(maxs-1)