def seven(n):
    if len(jo)==M:
        print(*jo)
        return
    for i in range(n,N):
        jo.append(num_li[i])
        seven(i)
        jo.pop()


N , M = map(int,input().split())
num_li = list(map(int,input().split()))
num_li.sort()
jo = []
seven(0)