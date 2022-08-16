T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int,input().split()))
    max = 0
    for i in number:
        if max < i :
            max = i
    print(f'#{test_case} {max}')