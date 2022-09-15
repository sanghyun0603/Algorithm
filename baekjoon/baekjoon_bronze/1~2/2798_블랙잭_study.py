#DFS 백트래킹

def dfs(n):
    if sum(card)>M:
        return
    if len(card)==3 and sum(card)<=M :
        maxne.append(sum(card))
        return
    for i in range(n,N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        card.append(num_li[i])
        dfs(i)
        card.pop()
        visited[i] =0

N,M = map(int,input().split())
num_li = list(map(int,input().split()))
visited = [0]*N
card = []
maxne = []
dfs(0)
print(max(maxne))