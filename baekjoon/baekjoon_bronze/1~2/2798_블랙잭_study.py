#DFS 백트래킹

def dfs(n):
    if sum(card)>M: # 합 보다 크면 절대 답이 될 수 없으니깐 백트래킹 1번
        return
    if len(card)==3 and sum(card)<=M : # 이경우가 3장의 카드를뽑아서 주어진 M에 최대한 가까운 값들
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