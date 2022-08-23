T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    li = [list(map(int,input().split())) for _ in range(M)]
    sums = 0
    for k in range(len(li)):
        for i in range(li[k][0],li[k][0]+li[k][2]):
            for j in range(li[k][1],li[k][1]+li[k][2]):
                if (0 <= i < N) and (0 <= j < N) :
                    sums += mat[i][j]
                    mat[i][j] = 0
    print(f'#{tc} {sums}')