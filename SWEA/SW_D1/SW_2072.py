T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int,input().split()))
    sum = 0
    i = 0
    while i < len(number):
        if number[i] % 2 == 1:
            sum += number[i]
        i += 1
    print(f'#{test_case} {sum}')