T = int(input())
for tc in range(1,T+1):
    cut = input()
    cnt = 0
    iron = 0
    i = 0
    while i <len(cut):
        if cut[i] == '(' and cut[i+1] == ')':
            cnt += iron
            i += 2 #레이저크기만큼
        elif cut[i] == '(':
            iron +=1
            i+=1
        elif cut[i] == ')':
            iron -=1
            cnt +=1 #쇠막대기 길이가 끝나 +1
            i+=1
    print(f'#{tc} {cnt}')
