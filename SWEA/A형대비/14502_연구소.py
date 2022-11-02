from collections import deque
def bfs(bits):
    Q = deque([])
    for i in bits:              # 벽 3개 세우기
        mat[i[0]][i[1]] = 1
    for k in virues:            # Q에 바이러스넣주기
        Q.append((k[0],k[1]))
    while Q:
        ii,jj = Q.popleft()
        for w in range(4):
            ni = ii + di[w]
            nj = jj + dj[w]
            if 0<=ni<N and 0<=nj<M and mat[ni][nj] == 0:
                mat[ni][nj] = 3
                Q.append((ni,nj))
    cnt = 0
    for i in range(N):          # 돌면서 0인 안전영역 세주고 3은 다시 0으로초기화
        for j in range(M):
            if mat[i][j] == 0:
                cnt += 1
            elif mat[i][j] == 3:
                mat[i][j] = 0
    for i in bits:              # 벽도 다시 부수기
        mat[i[0]][i[1]] = 0
    return cnt

def jo(n,a):
    global maxs
    if n == 3:
        ma = bfs(bits)              # 만든 조합 바탕으로 BFS 전부 다돌려봄.
        if maxs<ma:
            maxs =ma
        return

    for i in range(a,len(bincan)):  # 진짜 모든조합 다만듬. 테케하나에 5500가지되는것도있음
        if visited[i] == 0:
            visited[i] =1
            bits.append(bincan[i])
            jo(n+1,i+1)
            bits.pop()
            visited[i]=0

N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
bincan = []
virues = []
di = [1,-1,0,0]
dj = [0,0,1,-1]
maxs = 0                # 브루트포스 &BFS로 해결할거얌
for i in range(N):      # 빈칸 좌표,바이러스 좌표들 다 빼자.
    for j in range(M):
        if mat[i][j] == 0:
            bincan.append([i,j])
        elif mat[i][j] == 2:
            virues.append([i,j])
visited = [0]* len(bincan)
bits = []
jo(0,0)                 # 빈칸 좌표들로 가능한 모든 조합만들기.
print(maxs)