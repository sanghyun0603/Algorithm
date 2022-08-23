T = int(input())
for tc in range(1,T+1):
    cnt = 0
    nu_cnt = 0
    N = int(input())
    carrot = list(map(int,input().split()))
    for i in range(len(carrot)):
        if i == len(carrot)-1:
            if carrot[i]-1 == carrot[i-1]:
                cnt +=1
                nu_cnt = cnt
        elif carrot[i]+1 == carrot[i+1]:
            cnt +=1
        elif carrot[i]+1 != carrot[i+1] and cnt > 0:
            if carrot[i]-1 == carrot[i-1]:
                cnt+=1
                nu_cnt = cnt
                cnt = 0
            else:
                cnt = 0
    else:
        if nu_cnt == 0:
            nu_cnt =1
    print(f'#{tc} {nu_cnt}')
