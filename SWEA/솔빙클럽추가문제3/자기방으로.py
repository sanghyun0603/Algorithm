T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room1 = [0] *200            # 3번방으로 들어갈때 4번에서 나오는경우
                                #  400으로 해놓고 하면 경로가 겹치지 않는다.
                                # 이때 몫만 나타내는 //을 활용해서 해결하느냐
                                # 크기를 반으로 줄였다.
    for i in range(N):
        hy,re = map(int,input().split())
        if hy < re:             # (20,30) 등 일때
            hy = (hy - 1)// 2   # 1-3 경로 0, 1 4-6 경로 1,2 해서 겹침
            re = (re - 1)// 2
            for j in range(hy,re+1):# 학생이 돌아가는 경로에 1을더함
                room1[j] += 1       # 그럼 겹치는 경로가 생기는데
                                    # 이때 단위시간이 하나씩 증가
        elif hy > re:           # (30,20)등 큰방에서 작은방으로 이동할때
            hy,re = re, hy
            hy = (hy - 1) // 2
            re = (re - 1) // 2
            for j in range(hy, re+1):
                room1[j] += 1
    max_time = 0
    for i in room1:                 # 단위시간 구하기
        if max_time < i:
            max_time = i
    print(f'#{tc} {max_time}')
