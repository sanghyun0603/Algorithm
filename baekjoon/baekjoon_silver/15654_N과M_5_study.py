def dfs():
    if len(num_li) == M:
        print(*num_li)
        return
    for i in range(len(nums_li)):
        if visited[i] != 0:
            continue
        visited[i] = 1
        num_li.append(nums_li[i])
        dfs()
        num_li.pop()
        visited[i] = 0
N , M = map(int,input().split())
nums_li = list(map(int,input().split()))
nums_li.sort()
visited = [0]*N
num_li = []
dfs()