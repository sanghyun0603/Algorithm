T = int(input())
for test_case in range(1, T + 1):
    number = list(map(int,input().split()))
    a = round(sum(number)/len(number))
    print(f'#{test_case} {a}')