mat = [list(map(int,input().split())) for _ in range(19)]
cnt = 0
N = 19
suc = []
sucb = []
for i in range(N):
    if suc:
        break
    for j in range(N):
        if mat[i][j] == 1:
            dx=0
            cntr = cntu = cntd = cntru = cntrd = cntlu = cntld =0
            while dx+j < N:
                if mat[i][j+dx] == 1:
                    cntr += 1
                else:
                    break
                dx += 1
            if cntr == 5 :
                if j == 0:
                    suc.append(1)
                    suc.append(i+1)
                    suc.append(j+1)
                elif mat[i][j-1] != 1:
                    suc.append(1)
                    suc.append(i + 1)
                    suc.append(j + 1)
            dx = 0
            while i+dx < N:
                if mat[i+dx][j] == 1:
                    cntd += 1
                else:
                    break
                dx += 1
            if cntd == 5:
                if i == 0:
                    suc.append(1)
                    suc.append(i+1)
                    suc.append(j+1)
                elif mat[i-1][j] != 1:
                    suc.append(1)
                    suc.append(i + 1)
                    suc.append(j + 1)
            dx = 0
            while 0 <= i-dx:
                if mat[i-dx][j] == 1:
                    cntu += 1
                else:
                    break
                dx += 1
            if cntu == 5 :
                if i == 18:
                    suc.append(1)
                    suc.append(i-dx+2)
                    suc.append(j+1)
                elif mat[i+1][j] != 1:
                    suc.append(1)
                    suc.append(i - dx + 2)
                    suc.append(j + 1)
            dx = 0
            while 0 <= i-dx and j+dx <N:
                if mat[i-dx][j+dx] == 1:
                    cntru += 1
                else:
                    break
                dx += 1
            if cntru == 5:
                if j == 0:
                    suc.append(1)
                    suc.append(i+1)
                    suc.append(j+1)
                elif mat[i+1][j-1] != 1:
                    suc.append(1)
                    suc.append(i + 1)
                    suc.append(j + 1)
            dx = 0
            while i+dx < N and j+dx < N:
                if mat[i+dx][j+dx] == 1:
                    cntrd += 1
                else:
                    break
                dx += 1
            if cntrd == 5 :
                if j == 0 or i == 0:
                    suc.append(1)
                    suc.append(i+1)
                    suc.append(j+1)
                elif mat[i-1][j-1] != 1:
                    suc.append(1)
                    suc.append(i + 1)
                    suc.append(j + 1)
            dx = 0
            while 0 <= i-dx and 0<= j-dx:
                if mat[i - dx][j - dx] == 1:
                    cntlu += 1
                else:
                    break
                dx += 1
            if cntlu == 5:
                if i == 18 or j == 18:
                    suc.append(1)
                    suc.append(i-dx+2)
                    suc.append(j-dx+2)
                elif mat[i+1][j+1] != 1:
                    suc.append(1)
                    suc.append(i - dx + 2)
                    suc.append(j - dx + 2)
            dx = 0
            while i+dx < N and 0<= j-dx:
                if mat[i + dx][j - dx] == 1:
                    cntld += 1
                else:
                    break
                dx += 1
            if cntld == 5:
                if i == 0 or j == 18:
                    suc.append(1)
                    suc.append(i + dx )
                    suc.append(j - dx + 2)
                elif mat[i-1][j+1] != 1:
                    suc.append(1)
                    suc.append(i + dx)
                    suc.append(j - dx + 2)
for i in range(N): # 2번
    if sucb:
        break
    for j in range(N):
        if mat[i][j] == 2:
            dx=0
            cntr = cntu = cntd = cntru = cntrd = cntlu = cntld =0
            while dx+j < N:
                if mat[i][j+dx] == 2:
                    cntr += 1
                else:
                    break
                dx += 1
            if cntr == 5:
                if j == 0:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
                elif mat[i][j - 1] != 2:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
            dx = 0
            while i+dx < N:
                if mat[i+dx][j] == 2:
                    cntd += 1
                else:
                    break
                dx += 1
            if cntd == 5:
                if i == 0:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
                elif mat[i - 1][j] != 2:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
            dx = 0
            while 0 <= i-dx:
                if mat[i-dx][j] == 2:
                    cntu += 1
                else:
                    break
                dx += 1
            if cntu == 5:
                if i == 18:
                    sucb.append(2)
                    sucb.append(i - dx + 2)
                    sucb.append(j + 1)
                elif mat[i + 1][j] != 2:
                    sucb.append(2)
                    sucb.append(i - dx + 2)
                    sucb.append(j + 1)
            dx = 0
            while 0 <= i-dx and j+dx <N:
                if mat[i-dx][j+dx] == 2:
                    cntru += 1
                else:
                    break
                dx += 1
            if cntru == 5:
                if j == 0:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
                elif mat[i + 1][j - 1] != 2:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
            dx = 0
            while i+dx < N and j+dx < N:
                if mat[i+dx][j+dx] == 2:
                    cntrd += 1
                else:
                    break
                dx += 1
            if cntrd == 5:
                if j == 0 or i == 0:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
                elif mat[i - 1][j - 1] != 2:
                    sucb.append(2)
                    sucb.append(i + 1)
                    sucb.append(j + 1)
            dx = 0
            while 0 <= i-dx and 0<= j-dx:
                if mat[i - dx][j - dx] == 2:
                    cntlu += 1
                else:
                    break
                dx += 1
            if cntlu == 5:
                if i == 18 or j == 18:
                    sucb.append(2)
                    sucb.append(i - dx + 2)
                    sucb.append(j - dx + 2)
                elif mat[i + 1][j + 1] != 2:
                    sucb.append(2)
                    sucb.append(i - dx + 2)
                    sucb.append(j - dx + 2)
            dx = 0
            while i+dx < N and 0<= j-dx:
                if mat[i + dx][j - dx] == 2:
                    cntld += 1
                else:
                    break
                dx += 1
            if cntld == 5:
                if i == 0 or j == 18:
                    sucb.append(2)
                    sucb.append(i + dx)
                    sucb.append(j - dx + 2)
                elif mat[i - 1][j + 1] != 2:
                    sucb.append(2)
                    sucb.append(i + dx)
                    sucb.append(j - dx + 2)
if suc:
    print(suc[0])
    print(suc[1],suc[2])
elif sucb:
    print(sucb[0])
    print(sucb[1],sucb[2])
else:
    print(0)