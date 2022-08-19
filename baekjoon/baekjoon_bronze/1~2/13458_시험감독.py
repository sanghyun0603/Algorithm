import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
B ,C = map(int,sys.stdin.readline().split())
cnt = 0
for i in range(N):
    if A[i] - B < 1 :
        cnt += 1
    else:
        A[i] -= B
        cnt += 1
        if A[i]%C == 0:
            cnt += A[i]//C
        else:
            cnt += A[i]//C +1
print(cnt)