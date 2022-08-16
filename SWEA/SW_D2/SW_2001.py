T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    dimen = []
    kill = 0
    kill_2 = 0
    max = 0
    for repeat in range(N):
        fly = list(map(int,input().split()))
        dimen.append(fly)
    for x in range(N-M+1):
        for y in range(N-M+1):
            max_unkonown = 0
            for yy in range(y, y+M):
                for xx in range(x, x+M):
                    max_unkonown += dimen[yy][xx]
                    if max < max_unkonown:
                        max = max_unkonown
    print(f'#{test_case} {max}')

