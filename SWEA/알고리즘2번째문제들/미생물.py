from collections import deque
'''
1
7 2 3
2 4 8 1
1 3 6 4
1 5 7 3
'''

def bfs():
    mis = 0
    cnt = 0
    Q = deque([list(map(int, input().split())) for _ in range(K)])
    while cnt < M:
        cnt += 1
        check_li = []
        for m in range(len(Q)):
            i, j, mi, mo = Q.popleft()
            move = delta.get(mo)
            for_break = 0
            ni = i + move[0]
            nj = j + move[1]
            if 0 <= ni < N and 0 <= nj < N:
                if ni == 0 or ni == N - 1 or nj == 0 or nj == N - 1:
                    mi = mi // 2
                    if mo == 1:
                        mo = 2
                    elif mo == 2:
                        mo = 1
                    elif mo == 3:
                        mo = 4
                    elif mo == 4:
                        mo = 3
                    if mi != 0:
                        Q.append([ni, nj, mi, mo])
                else:
                    if check_li:
                        for i in range(len(check_li)):
                            if check_li[i][0] == ni and check_li[i][1] == nj:
                                    if max(check_li[i][2]) < mi:#맥스값몾찾는중
                                        check_li[i][3] = mo
                                        check_li[i][2].append(mi)
                                        for_break = 1
                                    else:
                                        check_li[i][2].append(mi)
                                        for_break =1
                        if for_break == 0:
                            check_li.append([ni, nj, [mi], mo])
                    else:
                        check_li.append([ni, nj, [mi], mo])
        for i in check_li:
            Q.append([i[0], i[1], sum(i[2]), i[3]])
    while Q:
        i, j, sums, mo = Q.popleft()
        mis += sums
    return mis


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # 행렬크기, 격리 시간, 미생물 군집의 개수
    # 1<= 이동범위 < N-1 이 밖으로 나가면
    # 절반되면서 방향 반대로
    delta = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}
    a = bfs()

    print(f'#{tc} {a}')
