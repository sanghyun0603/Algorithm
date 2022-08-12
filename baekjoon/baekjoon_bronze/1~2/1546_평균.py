N = int(input())
scores = list(map(int,input().split()))
maxs = max(scores)
for i in range(N):
    scores[i] = (scores[i]/maxs)*100
print(sum(scores)/N)