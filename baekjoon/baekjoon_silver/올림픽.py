N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)]
medal.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)#금메달,은메달,동메달순정렬
for i in range(N):#나라 넘버찾기
    if medal[i][0] == K:
        idx = i
# 같으면 공동 등수 이다.
for i in range(N):# 같은 메달이면 같은 등수
    if medal[idx][1:]==medal[i][1:]:
        rank =i+ 1
        break
print(rank)