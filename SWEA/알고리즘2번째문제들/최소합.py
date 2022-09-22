def dfs(i,j,s):
    global mins
    di =[1,0]
    dj = [0,1]
    if i == N-1 and j == N-1:
        if mins > s:
            mins = s
        return
    if s > mins:
        return
    for k in range(len(di)):
        ni = i+di[k]
        nj = j+dj[k]
        if 0<= ni<N and 0<= nj<N :
            dfs(ni,nj,s+mat[ni][nj])
T =int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mins = 999999
    dfs(0,0,mat[0][0])
    print(f'#{tc} {mins}')