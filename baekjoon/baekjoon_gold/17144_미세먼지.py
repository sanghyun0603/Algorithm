def munji():
    temp_li = [[0]*M for _ in range(N)]         # 퍼지는 먼지들 저장할 리스트
    for i in range(N):
        for j in range(M):
            if mat[i][j] !=0 and mat[i][j] != -1:   # 먼지들일때
                cnt = 0
                for w in range(4):                  # 사방으로 확산
                    ni = i + di[w]
                    nj = j + dj[w]
                    val = mat[i][j]//5              # 확산 값은 현재값/5의 소수점버림값
                    if 0<= ni<N and 0<= nj<M and mat[ni][nj] != -1:     # 공기청정기쪽으론 확산안함.
                        temp_li[ni][nj] += val
                        cnt += 1
                mat[i][j] -= (val*cnt)              # 현재값은 확산한방향만큼 깍임
    for i in range(N):                              # 확산후 값들 리스트에 저장
        for j in range(M):                          # 이렇게 하는이유 는 아래에.
            mat[i][j] += temp_li[i][j]

def air(i,j,cn):    # 어차피 공기청정기는 위아래 두개
    if cn == 0: # 위쪽바람
        dii = [0,-1,0,1]#오른쪽끝위왼쪽끝아래
        djj = [1,0,-1,0]
        dir = 0
        pre = 0
        while True:
            ni = i + dii[dir]
            nj = j + djj[dir]
            if 0<=ni<N and 0<=nj<M:     # 쭉쭉 가면서
                if mat[ni][nj] == -1:
                    break
                pre,mat[ni][nj] = mat[ni][nj],pre   # 한칸씩 미뤄준다. 이전값->현재값이 되고 현재값은 다음값의 이전값이된다.
            else:
                ni -= dii[dir]                      # 범위 벗어나면 방향 꺽는다.
                nj -= djj[dir]
                dir += 1
            i ,j = ni,nj                            # 그다음진행
    else:  # 아래쪽바람 위와 동일
        dii = [0, 1, 0, -1]  # 오른쪽끝아래왼쪽끝위
        djj = [1, 0 ,- 1, 0]
        dir = 0
        pre = 0
        while True:
            ni = i + dii[dir]
            nj = j + djj[dir]
            if 0 <= ni < N and 0 <= nj < M:
                if mat[ni][nj] == -1:
                    break
                pre, mat[ni][nj] = mat[ni][nj], pre
            else:
                ni -= dii[dir]
                nj -= djj[dir]
                dir += 1
            i, j = ni, nj
N,M,T = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
di = [1,-1,0,0]             # 먼지확산
dj = [0,0,1,-1]
air_machine = []            # 에어머신 위치 두곳 저장할리스트
ans = 0
for a in range(N):          # 에어머신 위치 저장
    if mat[a][0] == -1:
        air_machine.append([a,0])
for i in range(T):          # 1초마다 확산 -> 정화 과정 반복됨
    munji()                 # 확산.
    cn = 0
    for k in air_machine:
        air(k[0],k[1],cn)
        cn += 1

for i in range(N):      # 확산->정화과정을 T초만큼 거친 후 현재 먼지값 계산
    for j in range(M):
        if mat[i][j]>0:
            ans += mat[i][j]
print(ans)

# 확산하는 경우를 생각해보자.
# 40 20 이 확산하는경우를 생각하면 바로 리스트에 더해 버리면 40이 확산후 20은 28이 된다.
# 이렇게 되면 20은 확산할때 28//5의 값을 가지고 진행하면 5만큼이 확산되는데 주어진 문제에선 동시 확산이므로
# 20이 확산해서 4만큼이 확산이 돼야한다.
# 그래서 확산하는 먼지들만 모아놓는 리스트를 만들고
# 모든 확산이 다 끝나고 원래의 리스트에 더해주는것이다.