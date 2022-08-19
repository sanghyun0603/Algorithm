N , M = map(int,input().split())
num_list = list(map(int,input().split()))
mini = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            val = num_list[i]+num_list[j]+num_list[k]
            if val <= M and val > mini:
                mini = val
print(mini)

