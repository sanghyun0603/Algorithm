P, K = input().split()
P = int(P)
K = int(K)
count = 0
if P > K :
    while K <= P:
        count += 1
        K += 1
    print(count)
elif P < K :
    while K >= P:
        count += 1
        K -= 1
    print(count)
else :
    print('0')