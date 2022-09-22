# import sys
# sys.setrecursionlimit(10**6)
def dfs(i,j,cnt,string):
    global ans
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    if cnt == 0:
        if string not in num_li:
            num_li.add(string)
            ans += 1
        return
    for w in range(len(di)):
        ni = i+di[w]
        nj = j+dj[w]
        if 0<= ni<4 and 0<= nj <4:
            dfs(ni,nj,cnt-1,string+mat[ni][nj])

T = int(input())
for tc in range(1,T+1):
    mat = list(input().split() for _ in range(4))
    num_li = set()
    ans =0
    for i in range(4):
        for j in range(4):
            s= mat[i][j]
            dfs(i,j,6,s)
    print(f'#{tc} {ans}')