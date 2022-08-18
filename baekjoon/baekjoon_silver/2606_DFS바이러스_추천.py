

def dfs(v):
    visited[v] = 1
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

V = int(input())
E = int(input())
visited = [0] * V
adj_list = [[] for _ in range(V)]
for i in range(E):
    a,b = map(int,input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)
start = 0
dfs(0)
cnt = 0
for i in range(1,V):
    if visited[i] == 1:
        cnt += 1
print(cnt)