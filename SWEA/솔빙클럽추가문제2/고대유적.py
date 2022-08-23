T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    yu_max = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if mat[i][j] == 1:
                cnt += 1
            else:
                if yu_max < cnt:
                    yu_max = cnt
                cnt = 0
        if yu_max < cnt:
            yu_max = cnt
    for j in range(M):
        cnt = 0
        for i in range(N):
            if mat[i][j] == 1:
                cnt += 1
            else:
                if yu_max<cnt:
                    yu_max = cnt
                cnt = 0
        if yu_max < cnt:
            yu_max = cnt
    print(f'#{tc} {yu_max}')