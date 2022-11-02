def sun(n):             # tnsd
    if n ==N:
        print(*bits)
        return
    for i in range(1,N+1):
        if visited[i]==0:
            visited[i]=1
            bits.append(i)
            sun(n+1)
            bits.pop()
            visited[i]=0
N=int(input())
bits=[]
visited =[0]*(N+1)
sun(0)