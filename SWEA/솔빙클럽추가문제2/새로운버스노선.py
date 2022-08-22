T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_nosun = [list(map(int,input().split())) for _ in range(N)]
    bus = []
    max_no = 0
    for i in bus_nosun:
        if i[0] == 1 :
            for j in range(i[1]+1,i[2]):
                bus.append(j)
        if i[0] == 2 :
            if i[1]%2 == 0:
                for j in range(i[1]+1,i[2]):
                    if j%2 == 0:
                        bus.append(j)
            else:
                for j in range(i[1]+1,i[2]):
                    if j%2 == 1:
                        bus.append(j)
        if i[0] == 3:
            if i[1]%2 == 0:
                for j in range(i[1]+1,i[2]):
                    if j%4 == 0:
                        bus.append(j)
            else:
                for j in range(i[1]+1,i[2]):
                    if j%3 ==0 and j%10 != 0:
                        bus.append(j)
    for i in range(1,1001):
        cnt = 0
        for j in bus:
            if i == j :
                cnt += 1
        if max_no < cnt:
            max_no = cnt
    print(f'#{tc} {max_no}')