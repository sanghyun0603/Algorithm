def six(n):
    if len(jo)==M:
        print(*jo)
        return
    for i in range(a):
        if visited[i] == 1:
            continue
        visited[i] = 1
        jo.append(num_li[i])
        six(i)
        jo.pop()
        visited[i] =0


N , M = map(int,input().split())
num_li = list(map(int,input().split()))
num_li = set(num_li)
num_li = list(num_li)
num_li.sort()
a = len(num_li)
visited = [0]*a
jo = []
six(0)