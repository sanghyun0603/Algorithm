T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    max_kill = 0
    # 십자
    for i in range(N):
        for j in range(N):
            kill = 0
            for k in range(1,M):
                if 0<= i-k :
                    kill += mat[i - k][j]
                if N-1 >= i+k:
                    kill += mat[i+k][j]
                if N-1 >= j+k:
                    kill += mat[i][j+k]
                if 0 <= j-k:
                    kill += mat[i][j-k]
            kill += mat[i][j]
            if max_kill < kill:
                max_kill = kill
    #대각선
    for i in range(N):
        for j in range(N):
            kill = 0
            for k in range(1,M):
                if 0<= i-k and 0<= j-k:
                    kill += mat[i-k][j-k]
                if 0<= i-k and N-1 >= j+k:
                    kill += mat[i-k][j+k]
                if N-1 >= i+k and 0 <= j-k:
                    kill += mat[i+k][j-k]
                if N-1 >= i+k and N-1 >= j+k:
                    kill += mat[i+k][j+k]
                else:
                    pass
            kill += mat[i][j]
            if max_kill < kill:
                max_kill = kill
    print(f'#{tc} {max_kill}')


