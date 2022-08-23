T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = []
    new_mat = [] #회전매트릭스
    ch = ''
    mat = [list(map(int,input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N-1,-1,-1):  # 90도 회전
            ch += str(mat[c][r])    # int형이면 숫자합이 나와 str형변환
        new_mat.append(ch)          # 회전배열에 더함
        ch = ''
    for r in range(N-1,-1,-1):      # 180도 회전
        for c in range(N-1,-1,-1):
            ch += str(mat[r][c])
        new_mat.append(ch)
        ch = ''
    for r in range(N-1,-1,-1):      # 270도 회전
        for c in range(N):
            ch += str(mat[c][r])
        new_mat.append(ch)
        ch = ''
    print(f'#{tc}')
    for r in range(N):              # 회전배열을 구할땐 90도 180도 270도
                                    # 순으로 구해서 출력할땐 그만큼 널뛰기를해 출력한다.
        print(new_mat[r],new_mat[r+N],new_mat[r+(2*N)])