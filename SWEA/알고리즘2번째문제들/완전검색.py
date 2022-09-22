def dfs(i,j,s):
    global mins
    if j == 0:
        if mins >s:
            mins = s
        return
    for k in range(1,N):
        if 0 not in visited[1:]:
            dfs(j, 0, s + mat[j][0])
        if mat[j][k] !=0 and visited[k] ==0:
            visited[k] = 1
            dfs(j,k,s+mat[j][k])
            visited[k] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mins = 9999999

    for i in range(1,N):
        visited = [0] * N
        visited[i] =1
        dfs(0,i,mat[0][i])
    print(f'#{tc} {mins}')
