for test_case in range(1,11):
    N=int(input())
    matrix = []
    palin = ''
    palin_c = ''
    count = 0
    for c in range(8):
        list1 = input()
        list1 = list(list1)
        matrix.append(list1)
    for c in range(8):
        for r in range(8-N+1):
            for p in range(N):
                palin += matrix[c][p+r]
                palin_c += matrix[p+r][c]
            if palin == palin[::-1]:
                count+=1
            palin =''
            if palin_c == palin_c[::-1]:
                count+=1
            palin_c=''
    print(f'#{test_case} {count}')
