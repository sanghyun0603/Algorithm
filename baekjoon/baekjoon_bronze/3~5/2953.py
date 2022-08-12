maxs =0
for i in range(5):
    sum_list = list(map(int,input().split()))
    maxxx = sum(sum_list)
    if maxs < maxxx:
        maxs = maxxx
        ma_idx = i+1
print(ma_idx,maxs)