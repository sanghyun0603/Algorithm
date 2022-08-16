T = 1
for tc in range(1, T + 1):
    N = int(input())
    apart = list(map(int,input().split()))
    result = 0
    for check in range(2,N-2):
        if apart[check]-apart[check-1]> apart[check]-apart[check-2]:
            left = apart[check]-apart[check-2]
        else:
            left = apart[check]-apart[check-1]
        if apart[check]-apart[check+1]> apart[check]-apart[check+2]:
            right = apart[check]-apart[check+2]
        else:
            right = apart[check]-apart[check+1]
        if right < 0 and left < 0:
            result += 0
        elif right < 0 or left < 0:
            result += 0
        elif right > left:
            result += left
        else:
            result += right
    print(f'#{tc} {result}')