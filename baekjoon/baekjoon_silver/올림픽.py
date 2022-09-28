N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)]
medal.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)
for i in range(N):
    if medal[i][0] == K:
        idx = i
# 같으면 공동 등수 이다.
for i in range(N):
    if medal[idx][1:]==medal[i][1:]:
        rank =i+ 1
        break
print(rank)