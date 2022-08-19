M = int(input())
N = int(input())
li = []
for i in range(M,N+1):
    if int(i**0.5)**2 == i:
        li.append(i)

if sum(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))