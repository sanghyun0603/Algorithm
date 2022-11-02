import sys
sys.stdin = open('sample_input (4).txt')
def dfs(check,mexi_cnt,line):
    global min_val,mexi
    if check == mexi_len:       # 순회 끝남
        if mexi < mexi_cnt:
            mexi = mexi_cnt
            min_val = line
        elif mexi == mexi_cnt:  # 최대 연결 멕시는 같지만 길이 다를수있음
            if min_val > line:
                min_val = line
        return

    i = mexis[check][0]
    j = mexis[check][1]
    for w in range(4):       # 코어 4방향탐색.
        if w == 0:              # 동쪽
            for_b = 0        # 만약 못가는길->막히거나 다른코어간경우 설정변수
            dj = 1
            while j+dj < N:
                if mat[i][j+dj] == 1:
                    for_b = 1
                    break
                dj += 1
            if for_b == 1:
                continue    # 못가는곳이면 스킵
            else:
                dj = 1
                while j+dj < N:
                    mat[i][j+dj] =1
                    line += 1
                    dj += 1
                dfs(check+1,mexi_cnt+1,line)
                dj = 1      # 갔다가 다시 되돌림 그래야 4방탐색가능
                while j+dj <N:
                    mat[i][j+dj] = 0
                    line -= 1
                    dj += 1
        elif w == 1:        #서쪽
            for_b = 0
            dj = 1
            while j-dj >= 0:
                if mat[i][j-dj] == 1:
                    for_b=1
                    break
                dj += 1
            if for_b == 1:
                continue
            else:
                dj = 1
                while j-dj >= 0:
                    mat[i][j-dj] = 1
                    line += 1
                    dj += 1
                dfs(check+1,mexi_cnt+1,line)
                dj = 1
                while j-dj >= 0:
                    mat[i][j-dj] = 0
                    line -= 1
                    dj += 1
        elif w == 2:            # 북쪽
            for_b = 0
            di = 1
            while i-di >= 0:
                if mat[i-di][j] == 1:
                    for_b=1
                    break
                di += 1
            if for_b == 1:
                continue
            else:
                di = 1
                while i-di >= 0 :
                    mat[i-di][j] = 1
                    line += 1
                    di += 1
                dfs(check+1,mexi_cnt+1,line)
                di = 1
                while i-di >= 0:
                    mat[i-di][j] = 0
                    line -= 1
                    di += 1
        elif w == 3:            # 남쪽
            for_b = 0
            di = 1
            while i+di < N:
                if mat[i+di][j] == 1:
                    for_b = 1
                    break
                di += 1
            if for_b == 1:
                continue
            else:
                di = 1
                while i+di < N:
                    mat[i+di][j] = 1
                    line += 1
                    di += 1
                dfs(check+1,mexi_cnt+1,line)
                di = 1
                while i+di < N:
                    mat[i+di][j] = 0
                    line -= 1
                    di += 1
    dfs(check+1,mexi_cnt,line)  # 4방향이 다막혀 for문 끝났을때.



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    #가장자리 제외하고 담기.
    mexis = []
    min_val = 0
    mexi = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if mat[i][j] == 1:
                mexis.append([i,j])
    mexi_len = len(mexis)
    dfs(0,0,0)
    print(f'#{tc} {min_val}')
