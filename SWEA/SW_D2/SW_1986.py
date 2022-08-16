T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    out = 0
    for num in range(1,N+1):
        if num % 2 == 1:
            out += num
        else:
            out -= num
    print(f'#{test_case} {out}')