T = int(input())
for tc in range(1,T+1):
    N = int(input())
    dok = [list(map(int,input().split())) for _ in range(N)]
    dok = sorted(dok ,key= lambda x : (x[1],x[0]))
    ended = 0
    cnt = 0
    for i in dok:
        start = i[0]
        end = i[1]
        if start >= ended:
            cnt +=1
            ended = end
    print(f'#{tc} {cnt}')