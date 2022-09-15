def dfs(n):
    if sum(seven) >100:
        return
    if len(seven) >7:
        return
    if len(seven) == 7 and sum(seven) == 100:
        seven.sort()
        for k in seven:
            print(k)
        exit(0)
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