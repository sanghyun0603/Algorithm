import sys
N = int(input())
num_li = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
num_li.sort(key=lambda x: (x[1],x[0]))
for i in num_li:
    print(*i)