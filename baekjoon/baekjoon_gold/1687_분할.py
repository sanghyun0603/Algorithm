import sys
def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x
def union(x, y):
    rep[find_set(y)] = find_set(x)

#최소신장트리
N,M = map(int,input().split())
N_li = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
N_li.sort(key=lambda x:x[2])
rep = [i for i in range(N+1)]
cnt = 0
total = 0
for v,u,w in N_li:
    if find_set(v) != find_set(u):
        if find_set(v)<find_set(u):
            union(u,v)
        else:
            union(v,u)
        total += w
        cnt += 1
        if cnt == N-2:
            break
print(total)
