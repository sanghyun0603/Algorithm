# import sys
# sys.stdin = open('sample_input (4).txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    di =[1,-1,0,0]
    dj =[0,0,1,-1]
    maxs = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 0:
                sti,stj = i,j # 시작위치 저장
                for k in range(0,4): #시작 방향 4곳
                    dir = k
                    val = 0       # 블록,
                    ni,nj = i+di[dir],j+dj[dir]
                    while True:
                        if ni < 0 or ni >= N or nj < 0 or nj >=N:   # 벽꿍
                            ni -= di[dir]   # index에러방지
                            nj -= dj[dir]
                            if dir == 0:
                                dir = 1
                            elif dir == 1:
                                dir = 0
                            elif dir == 2:
                                dir = 3
                            elif dir == 3:
                                dir = 2
                            val += 1
                        if mat[ni][nj]== 1:   # 1번블록
                            if dir == 0:
                                dir = 2
                            elif dir == 1:
                                dir = 0
                            elif dir == 2:
                                dir = 3
                            elif dir == 3:
                                dir = 1
                            val += 1
                        elif mat[ni][nj] == 2: # 2번블록
                            if dir == 0:
                                dir = 1
                            elif dir == 1:
                                dir = 2
                            elif dir == 2:
                                dir = 3
                            elif dir == 3:
                                dir = 0
                            val += 1
                        elif mat[ni][nj] == 3: # 3번블록
                            if dir == 0:
                                dir = 1
                            elif dir == 1:
                                dir = 3
                            elif dir == 2:
                                dir = 0
                            elif dir == 3:
                                dir = 2
                            val += 1
                        elif mat[ni][nj] == 4: # 4번블록
                            if dir == 0:
                                dir = 3
                            elif dir == 1:
                                dir = 0
                            elif dir == 2:
                                dir = 1
                            elif dir == 3:
                                dir = 2
                            val += 1
                        elif mat[ni][nj] == 5: #5번블록
                            if dir == 0:
                                dir = 1
                            elif dir == 1:
                                dir = 0
                            elif dir == 2:
                                dir = 3
                            elif dir == 3:
                                dir = 2
                            val += 1
                        elif 6<= mat[ni][nj] <=10:
                            for_b = 0
                            for w1 in range(N):
                                for w2 in range(N):
                                    if mat[w1][w2] == mat[ni][nj]:
                                        if w1== ni and w2==nj:
                                            pass
                                        else:
                                            ni = w1
                                            nj = w2
                                            for_b =1
                                            break
                                if for_b == 1:  #for문 탈출용
                                    break
                        elif mat[ni][nj] == -1:
                            break
                        if ni == sti and nj == stj:
                            break
                        ni += di[dir]
                        nj += dj[dir]
                    if maxs<val:
                        maxs = val
    print(f'#{tc} {maxs}')



