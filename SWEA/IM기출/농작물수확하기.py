T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mat = [list(map(int,input().split())) for _ in range(N)]
    mid = N//2
    i = 0
    for i in range(N):
        if mid-i < 0:
            continue
            for j in range(mid-i,mid+1+i):
                print(i,j)

        i += 1
