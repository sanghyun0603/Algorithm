def clean(r,c,dire):
    global cnt
    if mat[r][c] == 0 and visited[r][c] ==0:    #처음 들어가서 청소하자
        cnt += 1
        visited[r][c] = 1
    k = 1
    while True:
        dir = (dire+k)%4                        # 달팽이? 푼기억으로 비슷하게 진행
        ni = r + di[dir]                        # 탐색?하지마 가서 아니면 돌아와
        nj = c + dj[dir]
        if mat[ni][nj] == 0 and visited[ni][nj] == 0: # 맞으면 들어가
            clean(ni,nj,dir)
            break
        ni -= di[dir]                           # 아니면 돌아와라
        nj -= dj[dir]
        k += 1                                  # 왼쪽방향부터 쭉 둘러보다가
        if k == 5:                              # 다 둘러보고도 갈때가 없네?
            if dire == 0:                       # 그럼 현재 방향에서 뒤로 한칸 후진
                r +=1
                if mat[r][c] == 1:              # 후진했는데 벽이야
                    break                       # 끝내기
                k = 1                           # 벽이아니다. 그럼 후진한곳에서 다시 좌하우상 탐색
            elif dire == 1:
                c += 1
                if mat[r][c] == 1:
                    break
                k=1
            elif dire == 2:
                r -= 1
                if mat[r][c] == 1:
                    break
                k=1
            elif dire == 3:
                c -= 1
                if mat[r][c] == 1:
                    break
                k=1

N,M = map(int,input().split())
s_i,s_j,dir = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
di = [-1,0,1,0]# 탐색을 북서남동
dj = [0,-1,0,1]
cnt = 0
visited = [[0]*M for _ in range(N)] # 한번 청소한곳은 안간다.
if dir ==1:                         # 문제에서는 북동남서로 줘서 내가쓰기편하게 북서남동으로바꾸기
    dir = 3
elif dir == 3:
    dir = 1
clean(s_i,s_j,dir)                  #like dfs
print(cnt)
