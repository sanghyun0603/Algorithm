from collections import deque
def bfs(guyok):
    Q = deque([guyok[0]])
    visited= [0]*(N+1)
    visited[guyok[0]] = 1
    val = 0
    cnt = 0
    while Q:
        m = Q.popleft()
        val += ingu[m-1]
        for injub in arr[m]:
            if injub in guyok and visited[injub] == 0:
                cnt += 1
                visited[injub] = 1
                Q.append(injub)
    if cnt == len(guyok)-1:
        return val
    else:
        return 0

def jo(n,cnt):
    global ans
    if cnt == n:
        gu1 , gu2 = [],[]
        a = 1
        while a< N+1:       # 한쪽을구하면 나머지 한쪽도 구할수 있음.
            if visited[a] == 1:
                gu1.append(a)
            else:
                gu2.append(a)
            a += 1
        b,c =bfs(gu1),bfs(gu2)
        if b != 0 and c != 0:
            ans = min(ans,abs(b-c))
        return
    for w in range(cnt+1,N+1):      # 조합만들기
        if visited[w] ==0:
            visited[w]=1
            jo(n,cnt+1)
            visited[w]=0

N = int(input())
ingu = list(map(int,input().split()))# 0번리스트가 1번선거구
arr = [[] for _ in range(N+1)]
ans = 10**10
for i in range(N):
    inp = list(map(int,input().split()))
    arr[i+1] = inp[1:]
#모든 지역구 조합만들기 단 두개의 지역구를 위해선 최소 1개의 선거구필요
for i in range(1,N//2+1):# N이 6일때 12345 6이나 6 12345나 똑같음. 그래서반으로
    visited = [0]*(N+1)
    jo(i,0)

if ans == 10**10:
    print(-1)
else:
    print(ans)