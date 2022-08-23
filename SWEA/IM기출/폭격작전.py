import sys
sys.stdin = open('sample_input_bo.txt')
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    bomb = [list(map(int,input().split())) for _ in range(M)]
    dx = [-1,1,-1,1] # 상하좌우 움직임
    cnt = 0
    for k in range(len(bomb)):
        i, j = bomb[k][0],bomb[k][1]
        cnt += mat[i][j]
        mat[i][j] = 0
        for _ in range(bomb[k][2]):
            i = i + dx[0]
            if (0 <= i <N) :
                cnt += mat[i][j]
                mat[i][j] = 0
        i, j = bomb[k][0], bomb[k][1]
        for _ in range(bomb[k][2]):
            i = i + dx[1]
            if 0<= i < N :
                cnt += mat[i][j]
                mat[i][j] = 0
        i, j = bomb[k][0],bomb[k][1]
        for _ in range(bomb[k][2]):
            j = j + dx[2]
            if 0 <= j < N:
                cnt += mat[i][j]
                mat[i][j] = 0
        i, j = bomb[k][0], bomb[k][1]
        for _ in range(bomb[k][2]):
            j = j + dx[3]
            if 0 <= j < N:
                cnt += mat[i][j]
                mat[i][j] = 0
    print(f'#{tc} {cnt}')