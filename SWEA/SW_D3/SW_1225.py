for test_case in range(1, 11):
    T = int(input())
    password = list(map(int,input().split()))
    print(f'#{T}',end=' ')
    while True:
        for i in range(1,6):
            temp = password.pop(0)
            temp = temp-i
            if temp < 0 or temp == 0:
                break
            else:
                password.append(temp)
        if temp < 0 or temp == 0:
            temp = 0
            password.append(temp)
            break
    print(*password)