def dfs(n,s):
    global maxs
    for i in range(n,len(T_P_li)):
        if N+1 > T_P_li[i][0]+i:    # 일할수있는 범위 안넘어가게조절
            dfs(i+T_P_li[i][0],s+T_P_li[i][1])
        else:
            if i == len(T_P_li)-1:  # 만약 넘어갔는데 그게 마지막요일일이면
                if maxs<s:          # 바로 맥스값비교
                    maxs= s
                return
            else:
                dfs(i+1,s)          # 아직 뒤에 일할게남았으면 하루더해서 다시 탐색
    if maxs<s:                      # 마지막날까찌 알차게한경우
        maxs =s
    return


N = int(input())
T_P_li = [list(map(int,input().split())) for _ in range(N)]
maxs = 0
visited = [0]*(N)
dfs(0,0)
print(maxs)