T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = input()
    cnt = 0
    cnt_max = 0
    for i in nums:
        if i == '1':
            cnt +=1
        else:
            if cnt_max < cnt:
                cnt_max = cnt
            cnt = 0
    else:
        if cnt_max < cnt:
            cnt_max = cnt
    print(f'#{tc} {cnt_max}')
