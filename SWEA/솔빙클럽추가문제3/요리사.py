import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,11):
    N = int(input())
    Nmod_li = []
    mins = 100000
    mat =[list(map(int,input().split())) for _ in range(N)]
    for i in range(1<<N): #1000
        Nmod = []
        for j in range(N):
            if i & (1<<j):
                Nmod.append(j)
        if len(Nmod) == N//2:
            Nmod_li.append(Nmod)
    M = len(Nmod_li)//2
    for i in range(M):
        A_num = Nmod_li[M - 1 - i]
        B_num = Nmod_li[M + i]
        sumA = 0
        sumB = 0
        for j in range(N//2):
            for k in range(N//2):
                if j != k:
                    sumA += mat[A_num[j]][A_num[k]]
                    sumB += mat[B_num[j]][B_num[k]]
        if abs(sumA - sumB) < mins:
            mins = abs(sumA - sumB)
    print(f'#{tc} {mins}')