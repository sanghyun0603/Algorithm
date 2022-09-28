N= int(input())
debate = [list(map(int,input().split())) for _ in range(N)]
debate.sort(key= lambda x:(x[1],x[0]))
cnt = 0
end = 0
for i in debate:
    s = i[0]
    e = i[1]
    if s >= end:
        cnt += 1
        end = e

print(cnt)