def dfs(n):
    if sum(seven) >100: # 가지치기 한번
        return
    if len(seven) >7:   # 8명이상이면 가치지기 백트래킹 2번
        return
    if len(seven) == 7 and sum(seven) == 100: # 100이되는경우
        seven.sort()
        for k in seven:
            print(k)
        exit(0)                              # 7명이 100이되는경우
        return
    for i in range(n,9):
        if visited[i] == 1:
            continue
        visited[i] = 1
        seven.append(nan[i])
        dfs(i)
        seven.pop()
        visited[i] = 0
nan =[]
seven = []
for _ in range(9):
    nan.append(int(input()))
visited = [0]*9
dfs(0)