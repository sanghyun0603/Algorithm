T = int(input())
for test_case in range(1, T + 1):
    a, b = input().split()
    if a > b :
        print(f'#{test_case} >')
    elif a < b :
        print(f'#{test_case} <')
    else :
        print(f'#{test_case} =')
    