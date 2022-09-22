T= int(input())
for tc in range(1,T+1):
    contain , truck = map(int,input().split())
    contain_li = list(map(int,input().split()))
    truck_li = list(map(int,input().split()))
    move = min(contain,truck)
    contain_li.sort(reverse=True)
    truck_li.sort(reverse=True)
    kg = 0
    cnt = 0
    visited = [0]*contain
    #큰순서대로 넣는다.
    for i in truck_li:
        if cnt == move:
            break
        for j in range(len(contain_li)):
            if i < contain_li[j] :
                continue
            if visited[j]==1:
                continue
            visited[j] =1
            kg += contain_li[j]
            cnt +=1
            break
    print(f'#{tc} {kg}')
