def find_set(x):
    while x != rep[x]:
        x=find_set(rep[x])
    return x
def union(x,y):
    a= find_set(x)
    b= find_set(y)
    if a==b:
        return
    if a>b:
        rep[b] = a
    else:
        rep[a] = b
import sys
N,M = map(int,input().split())
rep = [i for i in range(N+1)]
for i in range(M):
    inp,x,y = map(int,sys.stdin.readline().split())
    if inp == 0 :
        union(x,y)
    else:
        if find_set(x) == find_set(y):
            print('YES')
        else:
            print('NO')
