N = int(input())
num_li = [list(map(int,input().split())) for _ in range(N)]
num_li.sort()
for i in num_li:
    print(*i)