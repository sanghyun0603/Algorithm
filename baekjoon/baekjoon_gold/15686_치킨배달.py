def cal(chi):   # 거리구하기
    dir_li = 0
    for k in home_li:
        min_dir = 10**10
        for x,y in chi:     # 집과 치킨집들중 가장 가까운거리
            dir =abs(x-k[0])+abs(y-k[1])
            if min_dir >dir:
                min_dir = dir
        dir_li += min_dir # 가까운 거리만 모아서
        if dir_li >ans:     #가지치기
            return 10**11           # 아무 큰값 리턴
    return dir_li  # 그 합을 리턴

def jo(n):
    global ans
    if len(bits) ==M:       # 최대M개일때
        mins = cal(bits)
        if ans >mins:       # 최소값찾기
            ans = mins
        return
    for i in range(n,len(chi_li)):  # 조합만들기
        if visited[i] == 0:
            visited[i] =1
            bits.append(chi_li[i])
            jo(i+1)
            bits.pop()
            visited[i] = 0
N,M = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
home_li = []
chi_li = []
bits = []
ans = 10**10
for i in range(N):          #집과 치킨집들 위치 별도 저장
    for j in range(N):
        if mat[i][j] == 2:
            chi_li.append([i,j])
        elif mat[i][j] == 1:
            home_li.append([i,j])
visited = [0]*(len(chi_li))
jo(0)
print(ans)