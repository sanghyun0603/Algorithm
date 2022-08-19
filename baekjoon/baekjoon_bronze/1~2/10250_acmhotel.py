T = int(input())
for tc in range(1,T+1):
    H,W,N = map(int,input().split())
    hotel = []
    n = 1
    for i in range(1,W+1):
        for j in range(1,H+1):
            if i < 10 and n == N:
                print(str(j)+'0'+str(i))
            elif n == N:
                print(str(j)+str(i))
            n += 1
