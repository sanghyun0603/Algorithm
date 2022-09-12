def dfs(n): # 순열문제
    if len(num_li) == M:
        print(*num_li)
        return
    for i in range(n,N):
        num_li.append(i+1)
        dfs(i)
        num_li.pop()

N , M = map(int,input().split())
num_li = []
dfs(0)