import sys
sys.setrecursionlimit(10000)

def dfs(i,j):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[i][j] = 1
    for k in range(4):
        dj = j + dx[k]
        di = i + dy[k]
        if (0 <= dj < N) and (0 <= di < N):
            if visited[di][dj] == 0 and mat[di][dj] == 1:
                dfs(di,dj)
                dan_num[0] += 1

N = int(input())
mat = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dan_cnt = 0
dan_num = [0]
dan_nums = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and mat[i][j] == 1:
            dfs(i,j)
            dan_nums.append(dan_num[0]+1)
            dan_num = [0]
            dan_cnt += 1
print(dan_cnt)
dan_nums.sort()
for i in dan_nums:
    print(i)