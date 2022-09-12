def dfs():
    if len(num_li) == M:##길이가 M이면 출력후 리턴
        print(*num_li)
        return
    for i in range(N):
        if visited[i] != 0: # 중복없이라는 조건때문에 방문사용
            continue
        visited[i] = 1      # 방문하고
        num_li.append(i+1)  # 넣고
        dfs()               # 돌린후
        num_li.pop()        # 모든 조합을 봐야해서 빼고
        visited[i] = 0      # 그 방문을 초기화한다다N , M = map(int,input().split())
N , M = map(int,input().split())
visited = [0]*N             # 방문표시
num_li = []                 # 조합 담을 리스트
dfs()