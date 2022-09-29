N =int(input())
N_li = list(map(int,input().split()))
high_check = 0
mins_high =0
maxs_high =0
max_or = 0
for i in range(N-1):
    if N_li[i]<N_li[i+1] and high_check == 0:
        high_check = 1
        mins_high = N_li[i]
    if high_check == 1 and N_li[i]>=N_li[i+1]:
        maxs_high = N_li[i]
        max_or = max(max_or,(maxs_high-mins_high))
        high_check =0
if high_check == 1:
    maxs_high = N_li[-1]
    max_or = max(max_or,(maxs_high-mins_high))
print(max_or)