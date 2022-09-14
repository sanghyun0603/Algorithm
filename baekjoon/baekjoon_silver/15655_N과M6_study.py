def six(n):
    if len(jo)==M:
        print(*jo)
        return
    for i in range(n,N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        jo.append(num_li[i])
        six(i)
        jo.pop()
        visited[i] =0


N , M = map(int,input().split())
num_li = list(map(int,input().split()))
num_li.sort()
visited = [0]*N
jo = []
six(0)