def jo(joli,s,n):
    global maxs
    if s >C:                        # 용기합보다 크면 버리기
        return
    else:                           #그외는
        val =0
        for i in bits:              # 계산값맞게 구하고
            val += i*i
        if maxs <val:               # 그중 맥스값을 구함.
            maxs = val
    for i in range(n,len(joli)):    # 조합 만드는과정.
        if visited[i] == 0:
            visited[i] = 1
            bits.append(joli[i])
            jo(joli,s+joli[i],i+1)
            bits.pop()
            visited[i] = 0
T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    maxs_li = []                # 어차피 2명이다. 모든가능한 맥스값들 구해서 최대값기준으로 비교하자.
    for i in range(N):
        for j in range(N):
            jo_li = []          # 조합리스트에 들어갈 값들.
            maxs = 0
            if j+M-1 < N:       # M개를 택할때 범위 체크
                for k in range(j,j+M):      #   행에서 j~j+M개씩
                    jo_li.append(mat[i][k])
                bits = []                   # 조합만들기용 리스트
                visited = [0]*(len(jo_li))  # 조합이기대문에 필요
                jo(jo_li,0,0)
                maxs_li.append([maxs,i,k])  # 그 조합들중 가장 큰 맥스값일때 맥스값과,위치정보를 넣어준다.
    maxs_li.sort(reverse=True)              # 맥스값중 가장 큰 맥스값을찾자.
    ans = maxs_li[0][0]                     # 일단 첫번째 맥스값 무조건 넣기
    for i in range(1,len(maxs_li)):         # 그외 비교
        if maxs_li[i][1] == maxs_li[0][1] and maxs_li[0][2]-M >= maxs_li[i][2]: #M범위가 안겹치면
            ans += maxs_li[i][0]                                                # 더하고 끝
            break
        elif maxs_li[i][1] != maxs_li[0][1]:        # 아닐경우에
            ans += maxs_li[i][0]
            break
    print(f'#{tc} {ans}')
