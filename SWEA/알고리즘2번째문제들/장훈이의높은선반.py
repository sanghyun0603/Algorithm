def bubu(n,r,st,s):
    global mins
    if r == 0:
        if s<B:
            return
        else:
            if mins> (s-B):
                mins = (s-B)
            return
    for i in range(st,n-r+1):
        pick.append(key_li[i])
        bubu(n,r-1,i+1,s+key_li[i])
        pick.pop()
T =int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    key_li = list(map(int,input().split()))
    mins =9999999
    for i in range(1,N+1):
        pick =[]
        bubu(N,i,0,0)
    print(f'#{tc} {mins}')
