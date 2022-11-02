import sys
N,K = map(int,input().split())
N_li = list(map(int,sys.stdin.readline().split()))
N_li.sort()
print(N_li[K-1])