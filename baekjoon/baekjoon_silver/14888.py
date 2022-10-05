def calc(n1,n2,idx):
    if idx == 0:
        return n1 + n2
    elif idx == 1:
        return n1 - n2
    elif idx == 2:
        return n1 * n2
    else:
        return int(n1 / n2)
def dfs(n,ans):
    print(ans)
    global maxs,mins
    if n == N:
        maxs = max(ans,maxs)
        mins = min(ans,mins)
        return
    for i in range(4):
        if yeon_li[i] != 0:
            yeon_li[i] -=1
            answer = calc(ans,N_li[n],i)
            dfs(n+1,answer)
            yeon_li[i] += 1
N = int(input())
N_li = list(map(int,input().split()))
yeon_li = list(map(int,input().split()))
maxs = -(10**8)
mins = +(10**8)
dfs(1,N_li[0])
print(maxs)
print(mins)