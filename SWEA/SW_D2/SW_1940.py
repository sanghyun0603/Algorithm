T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N = int(input())
    distance = 0
    velocity = 0
    for i in range(N):
        com_vel = list(map(int,input().split()))
        if com_vel[0] == 0 :
            distance += velocity
        elif com_vel[0] == 1 :
            velocity += com_vel[1]
            distance += velocity
        elif com_vel[0] == 2:
            if velocity > com_vel[1] :
                velocity -= com_vel[1]
                distance += velocity
            else:
                velocity = 0
                distance += velocity
    print(f'#{tc} {distance}')


