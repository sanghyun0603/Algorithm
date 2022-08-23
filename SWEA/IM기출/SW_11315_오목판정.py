import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 'o':
                dx=0
                cntr = cntu = cntd = cntru = cntrd = cntlu = cntld =0
                while dx+j < N:
                    if mat[i][j+dx] == 'o':
                        cntr += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while i+dx < N:
                    if mat[i+dx][j] == 'o':
                        cntu += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while 0 <= i-dx:
                    if mat[i-dx][j] == 'o':
                        cntd += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while 0 <= i-dx and j+dx <N:
                    if mat[i-dx][j+dx] == 'o':
                        cntru += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while i+dx < N and j+dx < N:
                    if mat[i+dx][j+dx] == 'o':
                        cntrd += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while 0 <= i-dx and 0<= j-dx:
                    if mat[i - dx][j - dx] == 'o':
                        cntlu += 1
                    else:
                        break
                    dx += 1
                dx = 0
                while i+dx < N and 0<= j-dx:
                    if mat[i + dx][j - dx] == 'o':
                        cntld += 1
                    else:
                        break
                    dx += 1
                temp_max =max(cntr,cntu,cntd,cntru,cntrd,cntlu,cntld)
                if temp_max >= 5:
                    cnt = 'YES'
    if cnt == 'YES':
        pass
    else:
        cnt = 'NO'
    print(f'#{tc} {cnt}')